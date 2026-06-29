"""Minimal LLM microservice: FastAPI + Claude with structured output.

A SWE-flavored starter: typed request/response, a warm client loaded once,
structured (schema-validated) output, basic logging, and error handling.

Run:  uvicorn app:app --reload
Docs: http://127.0.0.1:8000/docs
"""
from __future__ import annotations

import logging
import os
from contextlib import asynccontextmanager

import anthropic
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

logging.basicConfig(level=logging.INFO)
log = logging.getLogger("llm-service")

MODEL = os.getenv("MODEL", "claude-opus-4-8")

# --- client loaded ONCE at startup (not per request) ------------------------
clients: dict[str, anthropic.Anthropic] = {}


@asynccontextmanager
async def lifespan(_: FastAPI):
    if not os.getenv("ANTHROPIC_API_KEY"):
        log.warning("ANTHROPIC_API_KEY is not set — calls will fail.")
    clients["anthropic"] = anthropic.Anthropic()
    log.info("Anthropic client ready (model=%s)", MODEL)
    yield
    clients.clear()


app = FastAPI(title="LLM Service", version="0.1.0", lifespan=lifespan)


# --- API schema -------------------------------------------------------------
class ExtractRequest(BaseModel):
    text: str = Field(..., description="Unstructured text to extract from.")


class Contact(BaseModel):
    """The structured shape we force the model to return."""

    name: str | None = None
    email: str | None = None
    company: str | None = None
    summary: str = Field(..., description="One-sentence summary of the text.")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "model": MODEL}


@app.post("/extract", response_model=Contact)
def extract(req: ExtractRequest) -> Contact:
    """Extract structured contact info from free text — schema-guaranteed output."""
    client = clients["anthropic"]
    try:
        # tool-calling is the reliable way to force a JSON shape
        tool = {
            "name": "save_contact",
            "description": "Save the extracted contact fields.",
            "input_schema": Contact.model_json_schema(),
        }
        resp = client.messages.create(
            model=MODEL,
            max_tokens=512,
            tools=[tool],
            tool_choice={"type": "tool", "name": "save_contact"},
            messages=[{"role": "user", "content": f"Extract contact info:\n\n{req.text}"}],
        )
        for block in resp.content:
            if block.type == "tool_use":
                return Contact(**block.input)
        raise ValueError("model did not return a tool call")
    except anthropic.APIError as e:
        log.exception("Anthropic API error")
        raise HTTPException(status_code=502, detail=f"LLM upstream error: {e}") from e
    except Exception as e:  # noqa: BLE001 - surface a clean 500
        log.exception("extract failed")
        raise HTTPException(status_code=500, detail=str(e)) from e
