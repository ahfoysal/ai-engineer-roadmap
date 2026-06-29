# Phase 9 — MLOps & Production

**Goal:** Ship AI systems that survive contact with real users — deployed, monitored, reproducible, and cost-controlled. This is what separates a hobbyist from an engineer.
**Time:** 4–5 weeks.

> **You already have the DevOps base.** You know Docker, CI/CD, cloud, APIs, logging, secrets. This module is *not* a re-teach of any of that. It's the **ML/LLM-specific delta** — the handful of things that break when the thing you're shipping is a model or a prompt instead of deterministic code. Skim what you know; spend your time on observability, evals, and cost.

---

## 🎯 Outcomes
You can take a model/AI app from notebook to a deployed, monitored, maintainable production service — and you know *why an AI service needs more than a normal one*.

---

## 🧠 What's actually different about shipping AI

A normal service is deterministic: same input → same output, forever, until you change the code. An AI service violates almost every assumption your DevOps instincts are built on. Internalize these six, because every practice below exists to handle one of them:

- **Outputs are non-deterministic.** Same prompt, different answer (temperature, model updates, retrieval order). You can't assert `response == expected`. Your "tests" become **evals** — graded scores over a dataset, not pass/fail equality.
- **Quality degrades silently.** Code that worked yesterday works tomorrow. A model that worked yesterday can quietly get worse — the input distribution shifts (**drift**), a vendor swaps the model behind an API, your retrieval corpus goes stale. Nothing throws an exception. Your dashboard stays green while answers rot. You only find out from users.
- **Cost is per-request and variable.** A normal endpoint costs ~the same per call. An LLM call costs *tokens*, and tokens scale with input + output length. One user pasting a 50-page PDF, or an agent that loops, can 100× your bill in a night. Cost is a first-class metric, not an afterthought.
- **Latency is high and bursty.** Seconds, not milliseconds. Cold model loads, large generations, and multi-step agents make p95 ugly. Streaming, caching, and timeouts matter more than usual.
- **Models and prompts are artifacts.** The "code" includes model weights, a prompt template, retrieval config, and the eval set. All of those need **versioning** — a prompt change is a deploy, even if no `.py` file changed.
- **Evals are your test suite.** No eval gate = no safety net. This is the single biggest mindset shift. You don't ship because tests pass; you ship because the eval score didn't regress.

---

## 🚀 Serving: getting the model behind an endpoint

You know FastAPI. The ML-specific parts:

- **Model loading & warm starts.** Load weights/clients **once at startup**, not per request. In FastAPI use a lifespan handler (or module-level singleton). A cold container that loads a 7B model on the first request will time out. Keep at least one warm instance; scale-to-zero saves money but reintroduces cold starts — know the trade.
- **Batch vs real-time.** Real-time = one request, low latency, user waiting. **Batch** = score a million rows overnight, throughput over latency, far cheaper. Pick deliberately; a lot of "ML inference" should be a nightly batch job, not a live endpoint.
- **LLM inference servers (awareness).** If you self-host open models, you don't write the serving loop — you run **[vLLM](https://github.com/vllm-project/vllm)** or **[TGI](https://github.com/huggingface/text-generation-inference)**. They give you continuous batching, paged KV-cache, and an OpenAI-compatible API, which is the difference between 5 and 50 req/s on the same GPU.
- **Managed inference vs self-host.** Calling OpenAI/Anthropic/Bedrock = zero ops, pay per token, vendor owns latency and model updates. Self-hosting open weights = you own the GPU bill and the ops, but get data control, no per-token markup at scale, and version pinning. Default to **managed** until cost or data-residency forces self-host.

---

## 📦 Packaging & deploy — the ML gotchas

Docker you know. What bites ML containers specifically:

- **Heavy dependencies.** `torch` + CUDA + transformers is multiple GB. Use slim base images, multi-stage builds, and don't `pip install` the GPU stack if you're only calling an API. Pin everything with a lockfile (`uv`, `pip-tools`) — "works on my machine" is worse when a transitive CUDA mismatch is silent.
- **GPU containers.** Need the NVIDIA Container Toolkit, a CUDA-matched base image (`nvidia/cuda`, `pytorch/pytorch`), and `--gpus all` at runtime. The image's CUDA version must match the host driver.
- **Model weights — don't bake big weights into the image.** A multi-GB image is slow to build, push, and cold-start. Mount weights from a volume, pull from object storage / HF Hub at startup, or use a platform that caches them. Version the weights separately from the code.
- **Cold starts.** First request after a scale-up pays for image pull + weight load + CUDA init. Mitigate with min-replicas ≥ 1, pre-warming, or platforms with snapshotting (Modal).

**Deploy targets — match the job:**
- **[Modal](https://modal.com/)** — serverless GPU, fast cold starts, great for inference and batch; Python-native.
- **[Hugging Face Spaces](https://huggingface.co/spaces)** — fastest path to a public demo (Gradio/Streamlit), free CPU tier.
- **[Railway](https://railway.app/) / Render / Fly.io** — simple container hosting for CPU APIs and demos.
- **AWS / GCP / Azure** — SageMaker, Vertex AI, Bedrock, ECS/GKE; pick when you need org infra, VPC, or scale.

---

## 🔬 MLOps practices — reproducibility & versioning

Beyond app code, you now have *experiments, data, and models* to track:

- **Experiment tracking** — **[Weights & Biases](https://wandb.ai/)** / **[MLflow](https://mlflow.org/)**. Log every run's params, metrics, and artifacts so "the model from last Tuesday that scored 0.91" is recoverable. For LLM work this also means logging which prompt + model + eval scored what.
- **Data & model versioning** — **[DVC](https://dvc.org/)** (or git-lfs / lakeFS) tracks large files by hash in git while the bytes live in object storage. Reproducibility means: commit hash → exact code + data + weights + prompt.
- **Model registry** — a catalogue of versioned models with stages (`staging`, `production`) and lineage. MLflow Registry, W&B, or SageMaker. This is what your deploy pipeline promotes from.
- **CI/CD adapted for ML.** Your pipeline tests **more than code**: it validates data schemas, runs the prompt/agent against an eval set, and gates the deploy on the score. Tests now cover data, prompts, and evals — not just functions.

---

## 👀 LLMOps & observability — the part SWEs underbuild

This is the new discipline, and it's where most AI products fail in production. Traditional logging tells you *the request happened*. LLMOps tells you *whether the answer was any good, what it cost, and why it was slow*.

- **Log prompts + responses.** Capture the full rendered prompt, the model output, token counts, latency, model/version, and a request id. You cannot debug an LLM bug you can't replay. (Redact PII — see Security.)
- **Tracing** — **[Langfuse](https://langfuse.com/)** / **[LangSmith](https://www.langchain.com/langsmith)**. A single user request fans out into retrieval → prompt assembly → model call → tool calls → re-prompt. A trace shows the whole tree with per-step latency and cost. Indispensable for agents and RAG.
- **Monitor four things continuously:** **quality** (eval scores / user feedback / thumbs), **latency** (p50/p95), **cost** (tokens × price, per route and per user), **token usage** (input vs output, context growth).
- **Drift detection.** Watch input distribution and output-quality metrics over time. Sample real traffic, run an LLM-judge or human review on a slice, alert when scores trend down. This is the only way to catch silent degradation.
- **Semantic caching.** Cache by *meaning*, not exact string — embed the query, return a cached answer if a near-duplicate exists. Cuts cost and latency dramatically for FAQ-like traffic. (Plain exact-match caching helps too and is simpler.)
- **Reliability: retries, fallbacks, rate limiting.** Wrap calls in retries with backoff (providers 429 and 5xx constantly). Implement **model failover** — if the primary errors or times out, fall back to a secondary model/provider. Rate-limit per user to cap cost and abuse.
- **Guardrails.** Validate output structure (JSON schema), filter unsafe content, and bound the context/token budget so a runaway input can't blow up cost or latency.

---

## ✅ Eval pipelines in CI — gate deploys on quality

Treat prompts and agents like code that must pass tests, where "tests" are graded evals:

- Keep a versioned **eval set** (inputs + reference answers / rubrics) in the repo.
- On every PR that touches a prompt, model, or retrieval config, **run the evals** and compute a score (exact-match, LLM-as-judge, retrieval recall, etc.).
- **Block the merge/deploy if the score regresses** past a threshold. This is your **eval gate** — the LLM equivalent of "tests must be green."
- Track scores over time so you can see whether a "small prompt tweak" actually helped or quietly hurt.

```yaml
# .github/workflows/eval.yml — gate deploys on eval score
name: eval-gate
on: pull_request
jobs:
  evals:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: astral-sh/setup-uv@v3
      - run: uv sync
      - name: Run eval suite
        env:
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
        run: uv run python -m evals.run --dataset evals/data.jsonl --min-score 0.85
      # exits non-zero if score < 0.85 → PR blocked
```

## 🧩 Minimal production endpoint (logging + cache)

A real LLM endpoint is rarely "just call the model." It checks a cache, logs everything, and is replayable:

```python
# app.py — FastAPI wrapper: warm client, semantic-ish cache, structured logging
import time, hashlib, logging
from contextlib import asynccontextmanager
from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI

log = logging.getLogger("llm")
cache: dict[str, str] = {}            # swap for Redis / a semantic cache in prod
client: OpenAI | None = None

@asynccontextmanager
async def lifespan(app: FastAPI):
    global client
    client = OpenAI()                  # load ONCE at startup, not per request
    yield

app = FastAPI(lifespan=lifespan)

class Query(BaseModel):
    text: str

@app.post("/ask")
def ask(q: Query):
    key = hashlib.sha256(q.text.encode()).hexdigest()
    if key in cache:                   # cache hit = $0, ~0ms
        log.info("cache_hit key=%s", key)
        return {"answer": cache[key], "cached": True}

    t0 = time.perf_counter()
    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": q.text}],
        timeout=30,
    )
    answer = resp.choices[0].message.content
    cache[key] = answer

    log.info(                          # log cost + latency for observability
        "llm_call key=%s tokens_in=%d tokens_out=%d latency_ms=%d",
        key, resp.usage.prompt_tokens, resp.usage.completion_tokens,
        int((time.perf_counter() - t0) * 1000),
    )
    return {"answer": answer, "cached": False}
```

In real life you'd ship the structured log to Langfuse/W&B, back the cache with Redis (and a semantic variant), wrap the call in retries + a fallback model, and enforce a per-user rate limit. But the shape — *warm client, cache, log tokens + latency* — is the whole game.

---

## 🔒 Security — the AI-specific surface

You already manage secrets and auth. Add these:

- **API key management.** Provider keys are money. Never in code or client-side; load from a secrets manager / env, rotate, scope per service. A leaked key is a direct bill.
- **PII handling.** Prompts and responses often contain user data and *you are logging them*. Redact/anonymize before logging, control retention, and know whether your provider trains on your data (use no-train / zero-retention tiers for sensitive data).
- **Prompt injection at the app layer.** Untrusted input (user text, web pages, retrieved docs, tool outputs) can carry instructions that hijack your model. Defend in *your* code: separate system from user content, never feed raw tool output back as trusted instructions, constrain tool permissions, validate/parse outputs, and treat the model as an untrusted component when it can trigger actions.

---

## ⚠️ Pitfalls for SWEs

- **Treating it like a stateless, deterministic service.** It isn't. Equality assertions, "if it returns 200 it's fine," and no replay logging all fail here.
- **No cost monitoring.** Shipping without per-request token/cost tracking is how you get a surprise five-figure bill. Cost is a metric, alert on it.
- **No eval gate.** Changing a prompt and deploying because "it looked better in one test." Without a graded eval set you have no idea if you regressed.
- **No observability into prompts.** If you don't log the rendered prompt + response, every production bug is unreproducible.
- **Ignoring drift.** Green dashboards while answer quality rots. Sample and re-score real traffic.
- **Unbounded context/token costs.** Agents that loop, growing chat history, users pasting huge inputs — cap context length and add timeouts/iteration limits.

---

## 🔑 Key terms

- **LLMOps** — ops practices specific to LLM apps: prompt/response logging, tracing, quality+cost+latency monitoring, evals, guardrails.
- **Drift** — gradual change in input distribution or output quality over time that silently degrades a system with no error thrown.
- **Semantic cache** — caches responses by meaning (embedding similarity) rather than exact string match, so paraphrased queries hit the cache.
- **Model registry** — versioned catalogue of trained models with stages (staging/prod) and lineage that deploys promote from.
- **Experiment tracking** — recording every run's params, metrics, and artifacts (W&B/MLflow) for comparison and reproducibility.
- **Eval gate** — a CI check that runs an eval set and blocks deploy if the quality score regresses; the LLM analogue of "tests must pass."
- **Fallback (model failover)** — routing to a secondary model/provider when the primary errors, times out, or rate-limits.
- **Token cost** — per-request price driven by input + output token counts; the variable, scale-with-length cost unique to LLM serving.

---

## 📚 Best resources
- **Course** — [Made With ML by Goku Mohandas (free, gold standard)](https://madewithml.com/) · [Full Stack Deep Learning](https://fullstackdeeplearning.com/)
- **roadmap.sh** — [MLOps Roadmap](https://roadmap.sh/mlops)
- **Serving/packaging** — [FastAPI docs](https://fastapi.tiangolo.com/) · [Docker get started](https://docs.docker.com/get-started/) · [vLLM](https://github.com/vllm-project/vllm) · [Modal docs](https://modal.com/docs)
- **LLMOps / observability** — [Langfuse docs](https://langfuse.com/docs) · [LangSmith](https://www.langchain.com/langsmith)
- **Tracking & versioning** — [Weights & Biases](https://wandb.ai/) · [MLflow](https://mlflow.org/) · [DVC](https://dvc.org/)
- **Books** — *Designing Machine Learning Systems* by Chip Huyen **(essential — drift, monitoring, infra)** · *AI Engineering* by Chip Huyen (2025, the LLMOps-era follow-up)

## 🛠️ Phase project
**Productionize one earlier project** (your RAG app or agent from a previous phase) into a real, deployed service.

**Acceptance criteria — it's done when:**
- [ ] App is containerized with **Docker** (slim image, lockfile-pinned deps, weights not baked into a giant image).
- [ ] A **FastAPI** backend serves it, with the model/client loaded once at startup (warm).
- [ ] **Structured logging** of every request: rendered prompt, response, token counts, latency, model version, request id (PII redacted).
- [ ] **Monitoring/tracing** wired to Langfuse (or W&B/MLflow) showing quality, latency, **cost**, and token usage.
- [ ] A **cache** (exact or semantic) in front of the model, with hit-rate visible in your metrics.
- [ ] Reliability: retries with backoff + a **fallback model**, plus a per-user rate limit.
- [ ] A versioned **eval set** in the repo and a **GitHub Actions eval gate** that blocks the deploy if the score regresses.
- [ ] Deployed to a **public URL** (Modal / HF Spaces / Railway / cloud) that a stranger can hit.
- [ ] README documents the architecture, the eval results, and the cost-per-request.

This is the project that gets you hired — it proves you can ship AI, not just prototype it.

➡️ Next: [Phase 10 — Portfolio, Specialization & Interview Prep](10-career.md)
