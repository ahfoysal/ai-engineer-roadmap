# 📅 Track A — 14-Week AI Engineer Syllabus (for SWEs)

A concrete, week-by-week plan to go from software engineer → employable **AI/GenAI Engineer** in ~14 weeks at **10–15 hrs/week**. Built to pair with the [SWE → ML/AI track](swe-to-ml.md).

**How to use:** each week has a *focus*, *daily-ish tasks*, and a *deliverable*. Ship the deliverable before moving on — momentum > perfection. Check the boxes.

> Pace assumes ~2 hrs on weekdays + a longer build block on the weekend. Slower is fine; just don't skip the deliverables.

---

## 🧱 Block 1 — Data + LLM foundations (Weeks 1–3)

### Week 1 — Data fluency (skim, you're a SWE)
- [ ] Mon–Tue: NumPy arrays, broadcasting, vectorization ([Phase 2](../phases/02-data.md))
- [ ] Wed–Thu: Pandas — load, filter, `groupby`, merge, missing data
- [ ] Fri: Matplotlib/Seaborn basics
- [ ] Weekend: **Deliverable** → a notebook that loads a real CSV, cleans it, and produces 3 charts + 3 insights
- [ ] ML intuition primer: watch [Karpathy — Intro to LLMs (1hr)](https://www.youtube.com/watch?v=zjkBMFhNj_g)

### Week 2 — Calling LLMs like an engineer
- [ ] Mon: How LLMs generate text; tokens, context windows, pricing ([Phase 6](../phases/06-llms.md))
- [ ] Tue: First API calls (Claude / OpenAI) — temperature, max tokens, streaming
- [ ] Wed: **Structured output / JSON mode / tool calling** (this is the unlock for SWEs)
- [ ] Thu: System prompts, roles, prompt templates
- [ ] Fri–Weekend: **Deliverable** → a CLI tool that takes text and returns validated structured JSON (e.g. resume → structured fields), with retries on bad output

### Week 3 — Prompt engineering + evals
- [ ] Mon: Zero/few-shot, chain-of-thought
- [ ] Tue: Reducing hallucinations; prompt injection basics
- [ ] Wed: **Building an eval set** for your task (inputs + expected behavior)
- [ ] Thu: LLM-as-a-judge; tracking cost & latency
- [ ] Fri–Weekend: **Deliverable** → add an eval suite to Week 2's tool that proves it works on 15+ test cases. Version your prompts in git.

---

## 🔎 Block 2 — RAG, the hireable skill (Weeks 4–7)

### Week 4 — Embeddings & vector search
- [ ] Mon: What embeddings are; cosine similarity; semantic search ([Phase 7](../phases/07-ai-engineering-rag.md))
- [ ] Tue: Embedding models (OpenAI, BGE, sentence-transformers)
- [ ] Wed: Vector DBs — spin up Chroma or Qdrant locally
- [ ] Thu: Index documents, run similarity queries
- [ ] Weekend: **Deliverable** → a semantic search CLI over a folder of your own docs

### Week 5 — Build a RAG pipeline
- [ ] Mon: The RAG flow: ingest → chunk → embed → store → retrieve → generate
- [ ] Tue: **Chunking strategies** (size, overlap, semantic)
- [ ] Wed: Prompt construction with retrieved context + citations
- [ ] Thu: Handle PDFs / HTML / markdown ingestion
- [ ] Fri–Weekend: **Deliverable** → "Chat with your docs" v1 — ask questions, get cited answers

### Week 6 — Make RAG actually good
- [ ] Mon: Hybrid search (BM25 + semantic)
- [ ] Tue: Re-ranking (cross-encoder / Cohere Rerank)
- [ ] Wed: Query rewriting, metadata filtering
- [ ] Thu: **Evaluate retrieval** (RAGAS / precision@k) — measure before/after
- [ ] Weekend: **Deliverable** → upgrade v1 with hybrid + re-rank; document the measured improvement

### Week 7 — Ship the RAG app
- [ ] Mon–Tue: Wrap it in **FastAPI** (your home turf)
- [ ] Wed: Simple UI with Streamlit or Gradio
- [ ] Thu: Add caching + error handling
- [ ] Fri–Weekend: **Deliverable** → ⭐ deployed "Chat with your docs" with a public URL + great README + architecture diagram

---

## 🤖 Block 3 — Agents (Weeks 8–10)

### Week 8 — Agent fundamentals
- [ ] Mon: What makes an agent (LLM + tools + loop + goal) ([Phase 8](../phases/08-agents.md))
- [ ] Tue: Tool/function calling deep dive
- [ ] Wed: ReAct pattern; planning & decomposition
- [ ] Thu: Memory (short-term context vs long-term vector store)
- [ ] Reading: [Anthropic — Building Effective Agents](https://www.anthropic.com/research/building-effective-agents)
- [ ] Weekend: **Deliverable** → a single-agent tool-use loop (e.g. calculator + web search + file read)

### Week 9 — Real agents + orchestration
- [ ] Mon: Loop control, retries, error recovery, cost limits
- [ ] Tue: Multi-agent (orchestrator + workers) — awareness/build
- [ ] Wed: Observability/tracing (LangSmith / Langfuse)
- [ ] Thu: **MCP** — connect a tool/data source via Model Context Protocol
- [ ] Fri–Weekend: **Deliverable** → a research agent (search → read → synthesize → cite) with a trace

### Week 10 — Harden + evaluate the agent
- [ ] Mon: Guardrails, sandboxing dangerous tools, prompt-injection defense
- [ ] Tue–Wed: Build an eval set for agent task success; measure it
- [ ] Thu–Weekend: **Deliverable** → ⭐ a useful, deployed agent with loop limits + tracing + an eval showing it succeeds

---

## 🚀 Block 4 — Production + getting hired (Weeks 11–14)

### Week 11 — ML/LLM production (the bits you don't have yet)
- [ ] Mon: LLM serving & inference concepts (vLLM/TGI awareness) ([Phase 9](../phases/09-mlops-production.md))
- [ ] Tue: **LLM observability** — logging, tracing, monitoring quality/latency/cost
- [ ] Wed: Semantic caching to cut cost; rate limits, fallbacks
- [ ] Thu: Drift & quality monitoring for LLM apps
- [ ] Weekend: **Deliverable** → add full observability + caching to your RAG app or agent

### Week 12 — Productionize the flagship
- [ ] Mon–Tue: Dockerize + clean dependency management (uv/lockfiles)
- [ ] Wed: GitHub Actions CI (lint, test, build)
- [ ] Thu: Deploy to cloud (Modal / HF Spaces / Railway / AWS) with secrets management
- [ ] Fri–Weekend: **Deliverable** → ⭐⭐ one flagship project fully productionized, monitored, live

### Week 13 — Portfolio + profile
- [ ] Mon: Polish 3–4 project READMEs (problem, stack, diagram, demo, learnings)
- [ ] Tue: Pin repos; clean GitHub profile
- [ ] Wed–Thu: Write 2 short build write-ups (blog/LinkedIn)
- [ ] Fri: Tune resume for AI Engineer (projects + metrics + your SWE production edge)
- [ ] Weekend: **Deliverable** → portfolio page/profile that tells a clear "SWE who ships AI" story

### Week 14 — Interview prep + apply
- [ ] Mon: ML/LLM concepts review ([interview/PREP.md](../interview/PREP.md)) — prompting vs RAG vs fine-tune, how RAG/agents work, eval
- [ ] Tue: ML system design out loud ("design a RAG system at scale", "design a support agent")
- [ ] Wed: Project deep-dive practice — explain every decision in 5 min
- [ ] Thu: Behavioral STAR stories + "why AI"
- [ ] Fri+: **Deliverable** → start applying. Lead with deployed projects + production strength.

---

## 🎓 After Week 14
- You have **3–4 deployed projects**, a production-grade flagship, and interview reps.
- **Backfill depth** with [Track B](swe-to-ml.md#-track-b--ml-engineer-add-this-for-depth-2-3-months) (math → classical ML → deep learning → transformers) while you interview.
- Keep one habit: reproduce one new paper/model per quarter.

⬅️ Back to [SWE track](swe-to-ml.md) · [README](../README.md)
