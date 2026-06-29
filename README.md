# 🔁 Software Engineer → AI / ML Engineer Roadmap (2026)

> A focused path for **people who already ship software** and want to become an **AI/ML Engineer**. This is **not** a "learn to code from zero" roadmap — it starts from where a working developer already is and spends your time only on what's actually new.

You already know how to write code, use Git, build APIs, ship to production, and reason about systems. That's a huge head start — the hardest part of being an **AI Engineer** (vs a researcher) is the *engineering*, and you have it. This roadmap skips what you know and goes straight to the ML/AI-specific skills.

**Time:** ~3–5 months at 10–15 hrs/week (AI Engineer track). Add ~2–3 months for deep ML.

---

## ✅ Assumed knowledge (you already have this — don't relearn it)

If you can do most of these, you're the target reader. **Skip** the foundations grind.

- Python (or you can pick it up fast), clean code, OOP
- Git / GitHub, branching, PRs
- Terminal, package management, virtual envs
- SQL and working with APIs / JSON
- Docker, building & deploying services
- CI/CD, testing, logging, cloud basics
- Reading docs, debugging, system design

> 🟢 **This background is your superpower.** Most ML grads ship a notebook; you can ship a tested, containerized, monitored, deployed service. Lead with that.

If some of the above are shaky, the [reference modules](#-reference-modules) below cover them — dip in as needed, don't do them front-to-back.

---

## 🆕 What's actually new for you

This is where your time goes:

1. **ML intuition** — how models learn, overfitting, evaluation (not heavy math).
2. **The LLM stack** — prompting, RAG, agents, evals. *This is the core of the AI Engineer job.*
3. **Just-enough deep learning** — so you're not a black-box user.
4. **ML-specific production** — model/LLM serving, drift, observability, cost, eval pipelines.

---

## 🛣️ The path (two tracks, both start from SWE)

### ⚡ Track A — AI / GenAI Engineer  *(recommended first — fastest to hired)*
Build products on top of models. Closest to your current skills; hottest 2026 market.

```text
  Step 1   Data fluency (skim)      → Pandas/NumPy enough to handle data
  Step 2   LLMs & GenAI             → APIs, prompting, structured output, evals
  Step 3   RAG & Vector DBs         → the #1 hireable AI skill
  Step 4   AI Agents                → tool use, orchestration, MCP
  Step 5   AI Production / LLMOps    → serving, observability, cost, eval pipelines
  Step 6   Portfolio + interviews    → ship deployed projects, get hired
```
**~3–4 months.** 👉 Follow the concrete plan: **[14-Week SWE→AI Engineer Syllabus](docs/track-a-syllabus.md)**

### 🧠 Track B — ML Engineer  *(add for depth, when you want to train/own models)*
Backfill the foundations once Track A has you building and employable.

```text
  Math (just-in-time)  →  Classical ML (real)  →  Deep Learning  →  NLP / Transformers
```
**+2–3 months.** You'll learn this *faster* because you're already building real things that need it.

> **Recommended order:** do **Track A first** (momentum + projects + job), then layer in **Track B** depth on the side. See [docs/which-path.md](docs/which-path.md).

---

## 📚 Reference modules

These are deep-dive modules, not a sequence to grind. Track A pulls from the 🆕 ones; tags show what to do given your SWE background.

- **Module 0 — [Programming Foundations](phases/00-foundations.md)** · ✅ *you have this — skip / use as checklist*
- **Module 1 — [Math & Statistics](phases/01-math-stats.md)** · 🔵 *skim, just-in-time (Track B)*
- **Module 2 — [Data Wrangling & Analysis](phases/02-data.md)** · 🟡 *skim — Pandas/NumPy you'll actually use*
- **Module 3 — [Classical Machine Learning](phases/03-classical-ml.md)** · 🔵 *Track B (real depth)*
- **Module 4 — [Deep Learning](phases/04-deep-learning.md)** · 🔵 *Track B (real depth)*
- **Module 5 — [NLP & Transformers](phases/05-nlp-transformers.md)** · 🔵 *Track B — understand attention*
- **Module 6 — [LLMs & Generative AI](phases/06-llms.md)** · 🆕 **core — Track A**
- **Module 7 — [RAG & Vector DBs](phases/07-ai-engineering-rag.md)** · 🆕 **core — Track A**
- **Module 8 — [AI Agents & Agentic Systems](phases/08-agents.md)** · 🆕 **core — Track A**
- **Module 9 — [MLOps & Production](phases/09-mlops-production.md)** · 🟡 *you know DevOps — add the ML/LLM-specific bits*
- **Module 10 — [Portfolio, Specialization & Interview Prep](phases/10-career.md)** · 🎯 *get hired*

**Legend:** ✅ already have · 🟡 skim/partial · 🔵 Track B depth · 🆕 core new skill · 🎯 career

---

## 🗂️ Repo contents

```
README.md                   ← you are here (SWE → AI/ML hub)
docs/swe-to-ml.md           ← the SWE → ML/AI strategy: what to skip, leverage, watch out for
docs/track-a-syllabus.md    ← 14-week week-by-week plan with daily tasks + deliverables
docs/which-path.md          ← AI Engineer vs ML Engineer vs Data Scientist
phases/00–10                ← reference modules (deep dives, checklists, resources, projects)
projects/PROJECTS.md        ← portfolio projects by difficulty
resources/RESOURCES.md      ← curated courses, books, channels, tools
interview/PREP.md           ← ML/AI interview prep
progress.md                 ← personal progress tracker
```

---

## ⚡ Leverage your SWE strengths

- **Production quality is your edge.** Ship tested, Dockerized, monitored, deployed AI services — not notebooks.
- **Build real apps.** Your portfolio should look like *software*: clean repos, CI, READMEs, live demos.
- **Treat prompts & evals like code.** Version them, test them, regression-check them. Rare and valued.
- **Read papers as specs.** Approach a new architecture like a new codebase.

## ⚠️ SWE blind spots to watch

- **ML is empirical, not deterministic.** "It compiles" ≠ "it works." You *evaluate*, you don't assert.
- **Data quality dominates** — more than model choice. Get comfortable being unglamorous with data.
- **Don't over-engineer.** Try a prompt before reaching for fine-tuning or a custom model.
- **Don't skip all intuition.** Understand evaluation, overfitting, and how transformers work — or you'll ship confidently-broken systems.

---

## 🚀 Start here

1. Read **[docs/swe-to-ml.md](docs/swe-to-ml.md)** — the strategy (10 min).
2. Open the **[14-Week Syllabus](docs/track-a-syllabus.md)** and start Week 1.
3. Track yourself in **[progress.md](progress.md)** and push every project to GitHub.

---

*Maintained by [@ahfoysal](https://github.com/ahfoysal). A practical path for developers moving into AI/ML. ⭐ if it helps.*
