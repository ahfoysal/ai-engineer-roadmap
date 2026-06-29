"""Minimal AI agent: an LLM in a while-loop with tools.

The whole idea of an agent in ~80 lines. The model decides which tool to call;
YOUR code executes it and feeds the result back; repeat until it answers.
Note the three things every agent needs: tool dispatch, a stop condition,
and a STEP LIMIT (no runaway cost). Pairs with Module 8.

Run:  python agent.py "What is 24 * 7 + 100, and what files are in this folder?"
"""
from __future__ import annotations

import json
import os
import sys
from pathlib import Path

import anthropic

MODEL = os.getenv("MODEL", "claude-opus-4-8")
MAX_STEPS = 8


# --- 1. Tools: a schema (what the model sees) + an impl (what your code runs) --
def calculator(expression: str) -> str:
    """Evaluate a basic arithmetic expression. (Real agents must sandbox this!)"""
    allowed = set("0123456789+-*/(). ")
    if not set(expression) <= allowed:
        return "error: only basic arithmetic is allowed"
    try:
        return str(eval(expression))  # noqa: S307 - constrained above; demo only
    except Exception as e:  # noqa: BLE001
        return f"error: {e}"


def list_files(directory: str = ".") -> str:
    try:
        return "\n".join(sorted(p.name for p in Path(directory).iterdir())) or "(empty)"
    except Exception as e:  # noqa: BLE001
        return f"error: {e}"


TOOLS = [
    {
        "name": "calculator",
        "description": "Evaluate a basic arithmetic expression like '2 * (3 + 4)'.",
        "input_schema": {
            "type": "object",
            "properties": {"expression": {"type": "string"}},
            "required": ["expression"],
        },
    },
    {
        "name": "list_files",
        "description": "List file names in a directory.",
        "input_schema": {
            "type": "object",
            "properties": {"directory": {"type": "string"}},
        },
    },
]
IMPLS = {"calculator": calculator, "list_files": list_files}


# --- 2. The agent loop -------------------------------------------------------
def run_agent(goal: str, max_steps: int = MAX_STEPS) -> str:
    client = anthropic.Anthropic()
    messages = [{"role": "user", "content": goal}]

    for step in range(max_steps):
        resp = client.messages.create(
            model=MODEL, max_tokens=1024, tools=TOOLS, messages=messages
        )
        messages.append({"role": "assistant", "content": resp.content})

        # stop condition: the model answered instead of calling a tool
        if resp.stop_reason != "tool_use":
            return "".join(b.text for b in resp.content if b.type == "text")

        # dispatch every tool call this turn, return results
        results = []
        for block in resp.content:
            if block.type == "tool_use":
                impl = IMPLS.get(block.name)
                out = impl(**block.input) if impl else f"error: unknown tool {block.name}"
                print(f"  [step {step+1}] {block.name}({json.dumps(block.input)}) -> {out!r}")
                results.append(
                    {"type": "tool_result", "tool_use_id": block.id, "content": out}
                )
        messages.append({"role": "user", "content": results})

    return f"(stopped: hit the {max_steps}-step limit without finishing)"


if __name__ == "__main__":
    goal = " ".join(sys.argv[1:]) or "What is 24 * 7 + 100?"
    print(run_agent(goal))
