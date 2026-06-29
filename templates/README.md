# 🧰 Starter Templates

Runnable scaffolds for the three core portfolio projects in this roadmap. Each is intentionally minimal but **real** — correct structure, typed, with an eval stub — so you can `pip install` and start building instead of wiring boilerplate.

| Template | Roadmap module | What it teaches |
|----------|----------------|-----------------|
| [`llm-service/`](llm-service/) | [Module 6 — LLMs](../phases/06-llms.md) | FastAPI + Claude, structured output, evals, Docker |
| [`rag-app/`](rag-app/) | [Module 7 — RAG](../phases/07-ai-engineering-rag.md) | ingest → chunk → embed → retrieve → cited answer |
| [`ai-agent/`](ai-agent/) | [Module 8 — Agents](../phases/08-agents.md) | tool-use loop with step limits |

## Conventions used in all three
- **Python 3.11+**, type hints, `requirements.txt` (swap for `uv`/`poetry` if you prefer).
- API keys via env var `ANTHROPIC_API_KEY` (use a `.env` + `python-dotenv` locally; never commit keys).
- Each has its own `README.md` with run instructions and "make it yours" next steps.
- Models default to `claude-opus-4-8` (swap to a Sonnet/Haiku id to trade quality for cost/speed).

> These are starting points, not finished portfolio pieces. The value is what *you* add: a real use case, an eval set that proves it works, and a deployment. See each template's README for the upgrade path.
