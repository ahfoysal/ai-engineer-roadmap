# 🔁 The Software Engineer → ML/AI Engineer Track

> You already write code, use Git, ship to production, and reason about systems. **Don't restart at zero.** This track leverages what you have and spends your time only on what's new.

This is the **fastest** route into AI/ML for an existing SWE: ~**3–5 months** at 10–15 hrs/week.

---

## ✅ What your SWE background already covers

You can **skip or skim** these — you have them:

| Roadmap topic | Your SWE status |
|---|---|
| Python, Git, CLI, packages ([Phase 0](../phases/00-foundations.md)) | ✅ Have it — skip |
| SQL, APIs, JSON | ✅ Have it — skip |
| Docker, FastAPI, CI/CD, testing, deployment ([Phase 9](../phases/09-mlops-production.md)) | ✅ Mostly have it — this is your **superpower**, just add the ML-specific bits |
| Reading docs, debugging, system design | ✅ Have it — transfers directly |
| Cloud, secrets, monitoring, logging | ✅ Have it |

> **This is a huge head start.** The hardest part of becoming an *AI Engineer* (vs researcher) is the engineering — and you already have it. Most ML grads are weak exactly where you're strong: shipping reliable production systems.

---

## 🎯 What's actually new for you

Focus your energy here:

1. **ML intuition** — how models learn, overfitting, evaluation (not deep math)
2. **The LLM stack** — prompting, RAG, agents, evals (your bread and butter as an AI Engineer)
3. **Just enough deep learning** — to not be a black-box user
4. **ML-specific production** — model serving, drift, LLM observability, eval pipelines

---

## 🛣️ Your accelerated path

### 🟢 Track A — AI/GenAI Engineer (recommended first, ~3–4 months)
Build LLM-powered products. Closest to your current skills, hottest market.

```
Week 1–2   Phase 2 (skim) — Pandas/NumPy enough to handle data
Week 2–4   Phase 6 — LLMs & GenAI: APIs, prompting, structured output, evals
Week 4–7   Phase 7 — RAG & Vector DBs (the #1 hire-able skill)
Week 7–10  Phase 8 — AI Agents, tool use, MCP
Week 10–14 Phase 9 — ML/LLM production bits you don't have (serving, eval, observability, cost)
ongoing    Phase 10 — portfolio + interviews (you already have GitHub muscle — use it)
```
👉 Skip Phases 0, 1, 3, 4, 5 for now. Skim them later for depth.

### 🔵 Track B — ML Engineer (add this for depth, +2–3 months)
When you want to train/own models, backfill the foundations:

```
Phase 1 (skim — just-in-time math)  →  Phase 3 (classical ML, real)  →
Phase 4 (deep learning, real)  →  Phase 5 (transformers)
```

> **Recommendation:** ship Track A first (get hireable + momentum + projects), then layer in Track B. You'll learn the foundations faster *because* you're already building real things that need them.

---

## ⚡ Leverage your SWE strengths

- **Make production quality your differentiator.** Where ML folks ship a notebook, you ship a tested, Dockerized, monitored, deployed service. Lead with that in interviews.
- **Build real apps, not toy notebooks.** Your portfolio should look like *software*: clean repos, CI, READMEs, live demos.
- **Treat prompts/evals like code.** Version them, test them, regression-check them. This instinct is rare and valued.
- **You can read papers as specs.** Approach a model/architecture like a new codebase.

## ⚠️ Watch out for SWE blind spots

- **ML is empirical, not deterministic.** "It compiles" ≠ "it works." You evaluate, you don't just assert. Embrace metrics and uncertainty.
- **Data quality dominates.** More than any model choice. Get comfortable being unglamorous with data.
- **Don't over-engineer.** Start with the simplest thing (a prompt) before reaching for fine-tuning or a custom model.
- **Don't skip *all* the intuition.** You can black-box a lot, but understand evaluation, overfitting, and how transformers work — or you'll ship confidently broken systems.

---

## 🛠️ Suggested first 3 projects (SWE-flavored)
1. **LLM API service** — FastAPI + Claude/OpenAI, structured output, an eval suite, Dockerized, deployed. (Plays to your strengths immediately.)
2. **RAG over a real codebase or docs** — ingestion pipeline, vector DB, cited answers, hybrid search + re-ranking, measured retrieval quality.
3. **An agent that does real work** — tool use, loop control, tracing/evals, maybe an MCP server. Production-grade.

Each one: clean repo, CI, README with architecture diagram, live URL. That portfolio gets a SWE hired as an AI Engineer.

---

## 📚 Highest-leverage resources for you
- [Karpathy — Intro to LLMs (1hr)](https://www.youtube.com/watch?v=zjkBMFhNj_g) — mental model fast
- [Anthropic — Building Effective Agents](https://www.anthropic.com/research/building-effective-agents)
- [DeepLearning.AI short courses](https://www.deeplearning.ai/short-courses/) — 1hr each, very SWE-friendly
- *AI Engineering* — Chip Huyen (2025) — written for exactly this transition
- [fast.ai](https://course.fast.ai/) — when you do Track B, it's code-first (suits you)

⬅️ Back to [README](../README.md) · See also [which-path.md](which-path.md)
