"""Minimal end-to-end RAG: ingest -> chunk -> embed -> store -> retrieve -> cited answer.

Local-first: sentence-transformers for embeddings (no API needed to index) and
Chroma as the vector store. Generation uses Claude. Everything you need to
understand RAG before reaching for a framework. Pairs with Module 7.

Usage:
    python rag.py index ./docs        # ingest a folder of .txt/.md files
    python rag.py ask "your question"
"""
from __future__ import annotations

import os
import sys
from pathlib import Path

import anthropic
import chromadb
from sentence_transformers import SentenceTransformer

MODEL = os.getenv("MODEL", "claude-opus-4-8")
EMBED_MODEL = "all-MiniLM-L6-v2"          # 384-dim, fast, runs locally
CHUNK_SIZE = 800                           # characters; tune against an eval set
CHUNK_OVERLAP = 120
TOP_K = 4

_embedder = SentenceTransformer(EMBED_MODEL)
_db = chromadb.PersistentClient(path=".chroma")
_col = _db.get_or_create_collection("docs")


def chunk(text: str, size: int = CHUNK_SIZE, overlap: int = CHUNK_OVERLAP) -> list[str]:
    """Fixed-size character chunks with overlap (the simple, solid default)."""
    chunks, start = [], 0
    while start < len(text):
        chunks.append(text[start : start + size])
        start += size - overlap
    return [c.strip() for c in chunks if c.strip()]


def index(folder: str) -> None:
    docs = list(Path(folder).rglob("*.txt")) + list(Path(folder).rglob("*.md"))
    if not docs:
        print(f"No .txt/.md files under {folder}")
        return
    ids, texts, metas = [], [], []
    for path in docs:
        for i, ch in enumerate(chunk(path.read_text(encoding="utf-8", errors="ignore"))):
            ids.append(f"{path}::{i}")
            texts.append(ch)
            metas.append({"source": str(path), "chunk": i})
    embeddings = _embedder.encode(texts, show_progress_bar=True).tolist()
    _col.upsert(ids=ids, documents=texts, embeddings=embeddings, metadatas=metas)
    print(f"Indexed {len(texts)} chunks from {len(docs)} files.")


def retrieve(question: str, k: int = TOP_K):
    q_emb = _embedder.encode([question]).tolist()
    res = _col.query(query_embeddings=q_emb, n_results=k)
    return list(zip(res["documents"][0], res["metadatas"][0]))


def ask(question: str) -> str:
    hits = retrieve(question)
    if not hits:
        return "Index is empty. Run: python rag.py index <folder>"
    # build a grounded prompt with numbered sources for citation
    context = "\n\n".join(f"[{i+1}] (source: {m['source']})\n{doc}" for i, (doc, m) in enumerate(hits))
    prompt = (
        "Answer the question using ONLY the context below. "
        "Cite sources inline like [1], [2]. If the answer isn't in the context, say you don't know.\n\n"
        f"Context:\n{context}\n\nQuestion: {question}"
    )
    client = anthropic.Anthropic()
    resp = client.messages.create(
        model=MODEL, max_tokens=700, messages=[{"role": "user", "content": prompt}]
    )
    answer = "".join(b.text for b in resp.content if b.type == "text")
    sources = "\n".join(f"  [{i+1}] {m['source']}" for i, (_, m) in enumerate(hits))
    return f"{answer}\n\nSources:\n{sources}"


if __name__ == "__main__":
    if len(sys.argv) >= 3 and sys.argv[1] == "index":
        index(sys.argv[2])
    elif len(sys.argv) >= 3 and sys.argv[1] == "ask":
        print(ask(" ".join(sys.argv[2:])))
    else:
        print(__doc__)
