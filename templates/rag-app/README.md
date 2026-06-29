# RAG App (starter)

A complete, framework-free **Retrieval-Augmented Generation** pipeline in ~90 lines: ingest → chunk → embed → store (Chroma) → retrieve → **cited** answer (Claude). Built to make [Module 7](../../phases/07-ai-engineering-rag.md) concrete *before* you reach for LangChain/LlamaIndex.

## Run

```bash
pip install -r requirements.txt
export ANTHROPIC_API_KEY=sk-ant-...

# 1) point it at a folder of .txt / .md files (your notes, docs, a wiki export)
python rag.py index ./docs

# 2) ask grounded questions — answers come back with [n] citations + sources
python rag.py ask "how do I reset my password?"
```

Embeddings run **locally** (sentence-transformers), so indexing needs no API key — only the answer step calls Claude.

## What this demonstrates
- The full RAG flow as plain code you can read and debug.
- Local embeddings + a persistent vector DB (`.chroma/`).
- **Grounded, cited generation** ("answer only from context, else say you don't know") — your main defense against hallucination.

## Make it yours (upgrade path → portfolio piece)
1. **Add PDFs/HTML ingestion** (`pypdf`, `trafilatura`) — real corpora aren't .txt.
2. **Measure retrieval** — build a small Q→expected-source set; compute precision@k. *This is what separates a real RAG engineer from a tutorial-follower.*
3. **Improve retrieval**: hybrid search (BM25 + dense) and a re-ranker; report the before/after numbers.
4. Try better chunking (recursive/semantic) and tune `CHUNK_SIZE`/`TOP_K` against your eval.
5. Wrap in FastAPI + a UI, then deploy with a live URL.

> Remember the Module 7 rule: when an answer is wrong, **first check what retrieval returned** — most RAG bugs are search bugs, not model bugs.
