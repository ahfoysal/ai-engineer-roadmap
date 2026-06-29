# Phase 7 — AI Engineering: RAG & Vector Databases

**Goal:** Give LLMs access to your own/private/up-to-date data through retrieval. This is the #1 most-requested AI engineering skill in industry.
**Time:** 3–4 weeks.

---

## 🎯 Outcomes
You can build a production-quality Retrieval-Augmented Generation (RAG) system, **measure** its retrieval quality, and know the concrete levers that make it accurate.

---

## 🧠 Mental model for SWEs

RAG = **give the LLM an open-book exam.**

Instead of relying on what the model memorized during training, you *retrieve* the relevant pages of your own data, *stuff* them into the prompt, and ask the model to answer **grounded** in that context — with citations.

```
question ──► retrieve relevant chunks ──► put chunks in prompt ──► LLM generates grounded answer
```

Two things follow from this that most engineers get wrong:

1. **RAG is a search problem bolted onto generation.** The "AI" part (calling the LLM) is the easy 10%. The hard 90% is retrieval: did you actually find the right chunks?
2. **Most RAG quality problems are *retrieval* problems, not LLM problems.** If the answer wasn't in the chunks you retrieved, no model — however large — can produce it. When a RAG answer is wrong, your first instinct should be "what did retrieval return?", not "let me try a bigger model."

Internalize this and you'll debug RAG 10x faster than people who treat it as a prompt-engineering exercise.

---

## 🔢 Embeddings explained

An **embedding** is a fixed-length vector of floats (e.g. 384, 768, or 1536 dimensions) that represents the *meaning* of a piece of text. A good embedding model places semantically similar texts close together in vector space.

```
"how do I reset my password" ──► [0.013, -0.21, 0.08, ... ]   (768 floats)
"forgot my login credentials" ──► [0.011, -0.19, 0.10, ... ]   (close by!)
"the capital of France"        ──► [0.91,  0.04, -0.77, ... ]  (far away)
```

**Cosine similarity** measures the angle between two vectors (range −1 to 1; closer to 1 = more similar). It ignores magnitude and looks only at direction, which is what you want for semantic comparison:

```
cos(a, b) = (a · b) / (‖a‖ · ‖b‖)
```

**Why semantic search beats keyword search:** keyword search (matching literal tokens) misses "forgot my login credentials" when the doc says "reset your password" — zero word overlap, same meaning. Embeddings capture that synonymy and paraphrase. (Keyword search still wins for exact terms, IDs, and rare jargon — which is why **hybrid search** exists; see below.)

**Embedding models to know:**
- **OpenAI** `text-embedding-3-small` / `-3-large` — strong, cheap, hosted API.
- **Cohere** `embed-v3` — strong multilingual, good with reranking.
- **Open-source** — [BGE](https://huggingface.co/BAAI) (BAAI) and [sentence-transformers](https://www.sbert.net/) (e.g. `all-MiniLM-L6-v2` for speed, `bge-large` for quality). Run locally, no per-call cost, full data control.

Rule: **embed the query and the documents with the same model.** Mixing models produces garbage similarity scores.

---

## 🔁 The full RAG pipeline, step by step

```
ingest → clean → chunk → embed → store → retrieve → rerank → build prompt → generate → cite
```

1. **Ingest** — pull source docs: PDFs, HTML, Markdown, code, Notion/Confluence, DB rows. Use parsers (e.g. `pypdf`, `unstructured`, `trafilatura` for HTML).
2. **Clean** — strip nav bars, boilerplate, page numbers, broken whitespace. Garbage in → garbage chunks → garbage retrieval.
3. **Chunk** — split docs into retrieval-sized pieces (see chunking below). This is the single highest-leverage design decision.
4. **Embed** — turn each chunk into a vector with your embedding model. Do this in batches.
5. **Store** — write `(vector, chunk text, metadata)` into a vector DB with an ANN index.
6. **Retrieve** — embed the user's query, do a nearest-neighbor search, get top-k chunks.
7. **Rerank** *(optional but high-impact)* — re-score the top-k (say top-50) with a heavier cross-encoder, keep the best (say top-5).
8. **Build prompt** — assemble a prompt: system instructions + retrieved chunks (with source IDs) + the question.
9. **Generate** — call the LLM, instructing it to answer **only** from the context and to say "I don't know" otherwise.
10. **Cite** — return source references so users can verify. Citations are your defense against hallucination and your debugging window into retrieval.

---

## ✂️ Chunking strategies in depth

Chunking decides what units of text are retrievable. Get it wrong and the right answer is split across two chunks, or buried in a 5,000-token wall of irrelevant text.

- **Fixed-size + overlap** — split every N tokens (e.g. 512) with an overlap (e.g. 50–100 tokens) so ideas straddling a boundary aren't lost. Simple, predictable, a fine default.
- **Recursive character splitting** — split on a hierarchy of separators (`\n\n` → `\n` → `. ` → ` `) to keep paragraphs/sentences intact, falling back only when a piece is still too big. This is LangChain's `RecursiveCharacterTextSplitter` and a great general default.
- **Semantic chunking** — embed sentences and cut at points where adjacent sentence embeddings diverge (topic shifts). Higher quality, more compute, more complexity.
- **Structure-aware** — split Markdown by heading, code by function/class, slides by slide. Respect the document's natural units.

How **chunk size** affects retrieval:
- **Too small** → high precision but fragments; an answer needing 3 sentences spans 3 chunks and only 1 gets retrieved.
- **Too large** → you retrieve a lot of irrelevant text, the embedding is "averaged out" and blurry, and you waste context window.
- Typical sweet spot: **256–1024 tokens** with **10–20% overlap**. Always tune empirically against an eval set.

**Attach metadata** to every chunk: `source`, `title`, `url`, `section`, `date`, `author`, `doc_type`. Metadata enables filtering ("only docs after 2024", "only from the API reference") and powers citations. Cheap to add, hugely valuable.

---

## 🗄️ Vector databases & ANN

Exact nearest-neighbor search over millions of vectors is too slow (it's a full scan). An **ANN** (Approximate Nearest Neighbor) index trades a tiny bit of recall for massive speed.

**HNSW** (Hierarchical Navigable Small World) is the most common ANN index: a multi-layer graph you traverse greedily from a coarse top layer down to fine layers, hopping toward closer neighbors. Sub-millisecond search over millions of vectors. Key knobs: `M` (graph connectivity), `ef_construction` (build quality), `ef_search` (query-time recall vs speed).

**When to pick which:**
- **Chroma** — dead-simple, embedded/local, great for prototyping and small apps. Start here while learning.
- **pgvector** — a Postgres extension. Pick this if you already run Postgres and want vectors *next to* your relational data with one system to operate. Scales well into the millions with HNSW.
- **Qdrant** — fast, Rust-based, excellent metadata filtering and hybrid support; easy self-host or cloud. Strong default for production self-hosting.
- **Pinecone** — fully managed, serverless, zero ops. Pick when you want to not run a database at all and are fine paying for it.
- **Weaviate** — feature-rich (built-in hybrid search, modules, GraphQL); good when you want batteries-included semantics.

Heuristic: **prototype on Chroma → ship on pgvector if you already have Postgres → reach for Qdrant/Pinecone/Weaviate when scale, hybrid, or managed ops justify it.**

---

## 💻 Code: minimal end-to-end RAG (sentence-transformers + Chroma)

```python
import chromadb
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")           # 384-dim, runs locally
client = chromadb.Client()
col = client.create_collection("docs")

docs = [
    "To reset your password, click 'Forgot password' on the login page.",
    "Our refund policy allows returns within 30 days of purchase.",
    "The API rate limit is 100 requests per minute per key.",
]
col.add(
    ids=[f"d{i}" for i in range(len(docs))],
    embeddings=model.encode(docs).tolist(),
    documents=docs,
    metadatas=[{"source": "help-center"} for _ in docs],
)

query = "I forgot my login credentials"
res = col.query(query_embeddings=model.encode([query]).tolist(), n_results=2)
print(res["documents"][0])   # -> the password-reset chunk ranks first
```

## 💻 Code: retrieval + prompt construction + grounded answer

```python
def build_prompt(question, chunks):
    context = "\n\n".join(
        f"[{i+1}] (source: {c['source']})\n{c['text']}" for i, c in enumerate(chunks)
    )
    return (
        "Answer the question using ONLY the context below. "
        "Cite sources as [n]. If the answer isn't in the context, say "
        "\"I don't know based on the provided documents.\"\n\n"
        f"Context:\n{context}\n\nQuestion: {question}\nAnswer:"
    )

chunks = [
    {"text": docs[0], "source": "help-center"},
    {"text": docs[2], "source": "api-docs"},
]
prompt = build_prompt("How do I get back into my account?", chunks)
# answer = llm.generate(prompt)   # plug in your provider's chat/messages API
```

---

## 🚀 Make RAG actually good (advanced)

These are the levers that move a demo into production quality:

- **Hybrid search (BM25 + dense)** — run keyword search (BM25) *and* vector search, then fuse the rankings (Reciprocal Rank Fusion). Dense catches paraphrase; BM25 catches exact terms, IDs, error codes, rare names. Hybrid almost always beats either alone.
- **Re-ranking** — retrieve a wide net (top-50) cheaply, then re-score with a **cross-encoder** that reads query+chunk *together* (e.g. `bge-reranker`, [Cohere Rerank](https://cohere.com/rerank)). Much more accurate than embedding similarity; you only run it on the shortlist. Often the single biggest quality win.
- **Query rewriting / expansion** — LLM-rewrite vague or conversational queries into clean search queries; generate query variants and union results; resolve pronouns from chat history before retrieving.
- **Metadata filtering** — constrain search by `date`, `doc_type`, `tenant_id`, permissions. Critical for multi-tenant apps and freshness.
- **Contextual retrieval** — before embedding each chunk, prepend a short LLM-generated description situating it within its parent document (e.g. "This section of the 2024 10-K discusses..."). Dramatically reduces failures from chunks that lost their context. See [Anthropic: Contextual Retrieval](https://www.anthropic.com/news/contextual-retrieval).

---

## 📊 Evaluation — you cannot improve what you don't measure

Treat RAG like any system: build a test set, measure, change one thing, re-measure.

**Build a RAG eval set:** collect 30–100 real questions, label which document(s)/chunk(s) *should* be retrieved, and write reference answers. This is the most valuable artifact in your whole project.

**Retrieval metrics** (does it find the right chunks?):
- **Precision@k** — of the top-k retrieved, what fraction are relevant.
- **Recall@k** — of all relevant chunks, what fraction appear in the top-k.
- **MRR** (Mean Reciprocal Rank) — `1/rank` of the first relevant result, averaged. Rewards putting the right chunk first.
- **Hit rate@k** — fraction of questions where *any* relevant chunk is in the top-k.

**Generation metrics** (is the answer good *given* the context?):
- **Faithfulness / groundedness** — is every claim in the answer supported by the retrieved context (no hallucination)?
- **Answer relevance** — does it actually address the question?
- **Context precision/recall** — did the retrieved context contain what was needed?

**[RAGAS](https://github.com/explodinggradients/ragas)** automates faithfulness, answer relevance, and context metrics using an LLM-as-judge. Wire it into CI.

**The discipline:** measure retrieval **before**, make one change (e.g. add hybrid + rerank), measure **after**. Keep the number. "It feels better" is not a result.

---

## ⚠️ Pitfalls for SWEs

- **Garbage chunking = garbage answers.** Poorly split or dirty chunks cap your ceiling no matter how good the LLM is. Spend your time here.
- **Not measuring retrieval.** Without an eval set you're tuning blind. Build one on day one.
- **Over-stuffing the context.** Dumping 50 chunks adds noise, dilutes attention, raises cost/latency, and *lowers* answer quality. Retrieve wide, rerank, keep few.
- **Stale indexes.** Source docs change; if you don't re-ingest, you confidently serve outdated answers. Plan reindexing/incremental updates.
- **Treating it as an LLM problem when it's a search problem.** Swapping models rarely fixes a retrieval miss. Inspect what was retrieved first.
- **Believing the model > the plumbing.** Chunk size, metadata, hybrid search, and reranking move quality far more than picking a fancier embedding or generation model.

---

## 🔑 Key terms

- **Embedding** — fixed-length vector encoding the meaning of text.
- **Vector DB** — store optimized for nearest-neighbor search over embeddings.
- **ANN** — Approximate Nearest Neighbor; fast, slightly-lossy similarity search.
- **HNSW** — graph-based ANN index; the common default for fast vector search.
- **Chunking** — splitting documents into retrieval-sized pieces.
- **Cosine similarity** — angle-based similarity between two vectors (−1 to 1).
- **Reranking** — re-scoring a candidate shortlist with a heavier cross-encoder.
- **Hybrid search** — combining keyword (BM25) and dense vector search.
- **Grounding** — answering strictly from retrieved evidence, with citations.
- **BM25** — classic keyword-ranking algorithm (TF-IDF family).

---

## ✅ Checklist

### Embeddings & vector search
- [ ] What embeddings are (text → vectors)
- [ ] Cosine similarity & semantic search; why it beats keyword
- [ ] Embedding models (OpenAI, Cohere, open-source [BGE](https://huggingface.co/BAAI), [sentence-transformers](https://www.sbert.net/))
- [ ] Vector databases: **[Chroma](https://www.trychroma.com/), [Qdrant](https://qdrant.tech/), [Pinecone](https://www.pinecone.io/), [Weaviate](https://weaviate.io/), pgvector** — and when to pick each
- [ ] ANN & **HNSW** indexing intuition

### The RAG pipeline
- [ ] Full pipeline: ingest → clean → chunk → embed → store → retrieve → rerank → prompt → generate → cite
- [ ] **Chunking strategies** (fixed+overlap, recursive, semantic, structure-aware)
- [ ] How chunk size & overlap affect retrieval
- [ ] Metadata design (filtering + citations)
- [ ] Retrieval + prompt construction (stuffing context, grounding, "I don't know")
- [ ] Handling documents: PDFs, HTML, code

### Making RAG actually good (advanced)
- [ ] Hybrid search (BM25 + dense, rank fusion)
- [ ] Re-ranking (cross-encoders, [Cohere Rerank](https://cohere.com/rerank))
- [ ] Query rewriting / expansion
- [ ] Metadata filtering
- [ ] Contextual retrieval ([Anthropic article](https://www.anthropic.com/news/contextual-retrieval))

### Evaluation
- [ ] Build a labeled RAG eval set (questions → expected chunks → reference answers)
- [ ] Retrieval metrics: precision@k, recall@k, MRR, hit rate
- [ ] Generation metrics: faithfulness/groundedness, answer relevance
- [ ] [RAGAS](https://github.com/explodinggradients/ragas) in your loop; measure before/after

### Frameworks
- [ ] [LlamaIndex](https://www.llamaindex.ai/) and/or [LangChain](https://www.langchain.com/)
- [ ] When to use a framework vs roll your own

---

## 📚 Best resources
- **Concepts** — [Pinecone Learning Center](https://www.pinecone.io/learn/) · [LlamaIndex docs](https://docs.llamaindex.ai/) · [LangChain docs](https://python.langchain.com/)
- **Embeddings/rerankers** — [sentence-transformers (SBERT)](https://www.sbert.net/) · [Cohere Rerank](https://cohere.com/rerank)
- **Courses** — [DeepLearning.AI: Building & Evaluating Advanced RAG](https://www.deeplearning.ai/short-courses/) · [LangChain: Chat with Your Data](https://www.deeplearning.ai/short-courses/langchain-chat-with-your-data/)
- **Deep dive** — [Anthropic: Contextual Retrieval](https://www.anthropic.com/news/contextual-retrieval)
- **Evaluation** — [RAGAS](https://github.com/explodinggradients/ragas)

---

## 🛠️ Phase project
**Build "Chat with your docs" — and prove it got better.** Ingest a real corpus (your notes, a codebase, company docs, a textbook). Implement chunking + embeddings + a vector DB + retrieval + cited answers.

**Acceptance criteria:**
1. End-to-end system returns **grounded, cited** answers and says "I don't know" when the corpus lacks the answer.
2. A **labeled eval set** of ≥30 questions with expected chunks/answers.
3. Reported **baseline** retrieval metrics (recall@k, MRR) and RAGAS faithfulness on dense-only retrieval.
4. Add **hybrid search + reranking** (and optionally contextual retrieval), then report the **after** numbers.
5. A short write-up of the before/after delta and which lever helped most.

➡️ Next: [Phase 8 — AI Agents & Agentic Systems](08-agents.md)
