# Phase 7 — AI Engineering: RAG & Vector Databases

**Goal:** Give LLMs access to your own/private/up-to-date data through retrieval. This is the #1 most-requested AI engineering skill in industry.
**Time:** 3–4 weeks.

---

## 🎯 Outcomes
You can build a production-quality Retrieval-Augmented Generation system and know how to make it accurate.

## ✅ Checklist

### Embeddings & vector search
- [ ] What embeddings are (text → vectors)
- [ ] Cosine similarity & semantic search
- [ ] Embedding models (OpenAI, Cohere, open-source [BGE](https://huggingface.co/BAAI), [sentence-transformers](https://www.sbert.net/))
- [ ] Vector databases: **[Pinecone](https://www.pinecone.io/), [Weaviate](https://weaviate.io/), [Qdrant](https://qdrant.tech/), [Chroma](https://www.trychroma.com/), pgvector**
- [ ] Indexing & similarity search (ANN, HNSW)

### Retrieval-Augmented Generation (RAG)
- [ ] The RAG pipeline: ingest → chunk → embed → store → retrieve → generate
- [ ] **Chunking strategies** (size, overlap, semantic chunking)
- [ ] Retrieval + prompt construction (stuffing context)
- [ ] Citations & grounding (reduce hallucination)
- [ ] Handling documents: PDFs, HTML, code

### Making RAG actually good (advanced)
- [ ] Hybrid search (keyword + semantic / BM25)
- [ ] Re-ranking (cross-encoders, [Cohere Rerank](https://cohere.com/rerank))
- [ ] Query rewriting / expansion
- [ ] Metadata filtering
- [ ] Evaluating RAG ([RAGAS](https://github.com/explodinggradients/ragas), retrieval precision/recall)
- [ ] Multi-modal & graph RAG (awareness)

### Frameworks
- [ ] [LangChain](https://www.langchain.com/) and/or [LlamaIndex](https://www.llamaindex.ai/)
- [ ] When to use a framework vs roll your own

## 📚 Best resources
- **Concepts** — [Pinecone Learning Center](https://www.pinecone.io/learn/) · [LlamaIndex docs](https://docs.llamaindex.ai/)
- **Courses** — [DeepLearning.AI: Building & Evaluating Advanced RAG](https://www.deeplearning.ai/short-courses/) · [LangChain Chat with Your Data](https://www.deeplearning.ai/short-courses/langchain-chat-with-your-data/)
- **Deep dive** — [Anthropic: Contextual Retrieval](https://www.anthropic.com/news/contextual-retrieval) · [RAG best practices papers]

## 🛠️ Phase project
**Build "Chat with your docs."** Ingest a real corpus (your notes, a codebase, company docs, a textbook). Implement chunking + embeddings + vector DB + retrieval + cited answers. Then **measure and improve** retrieval quality with hybrid search + re-ranking. Document the before/after.

➡️ Next: [Phase 8 — AI Agents & Agentic Systems](08-agents.md)
