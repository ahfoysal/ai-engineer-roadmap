# 🧠 AI / ML Engineer Roadmap 2026

> A complete, opinionated, **0 → job-ready** path to becoming an AI/ML Engineer — with checklists, weekly schedules, hands-on projects, and the best free + paid resources for every topic.

Most roadmaps stop at "learn the topics." This one is built as an actual **course you can follow**: each phase has clear goals, a checklist of skills, curated resources, a build project, and a time estimate. Check the boxes as you go.

Inspired by [roadmap.sh/ai-engineer](https://roadmap.sh/ai-engineer) — but broader. roadmap.sh focuses mostly on the **LLM-app layer**. This roadmap covers the **full stack**: programming → math → classical ML → deep learning → LLMs → agents → MLOps → getting hired.

---

## 🎯 Who this is for

- **Complete beginners** who can use a computer and want to become an AI/ML engineer.
- **Software engineers** pivoting into AI/ML → **start here:** [🔁 SWE → ML/AI track](docs/swe-to-ml.md) (skips what you already know, ~3–5 months).
- **Data analysts / scientists** who want to ship production AI systems.

You do **not** need a CS/math degree. You **do** need consistency: ~10–15 hrs/week for ~6–9 months.

> ### 👨‍💻 Already a software engineer?
> Don't restart at zero. The **[SWE → ML/AI Engineer track](docs/swe-to-ml.md)** leverages your existing Python/Git/Docker/deployment skills and focuses only on what's new (ML intuition + the LLM/RAG/agent stack). It's the fastest route in — and there's a concrete **[14-week week-by-week syllabus](docs/track-a-syllabus.md)** with daily tasks and deliverables.

---

## 🗺️ The roadmap at a glance

**11 phases, ~6–9 months at 10–15 hrs/week.** Click any phase to open it.

- **Phase 0 — [Programming Foundations](phases/00-foundations.md)** · Python, Git, CLI, SQL · _3–4 wks_
- **Phase 1 — [Math & Statistics](phases/01-math-stats.md)** · Linear algebra, calculus, probability · _3–4 wks_
- **Phase 2 — [Data Wrangling & Analysis](phases/02-data.md)** · NumPy, Pandas, EDA, visualization · _2–3 wks_
- **Phase 3 — [Classical Machine Learning](phases/03-classical-ml.md)** · scikit-learn, the core algorithms · _4–5 wks_
- **Phase 4 — [Deep Learning](phases/04-deep-learning.md)** · PyTorch, NN, CNN, RNN, training · _5–6 wks_
- **Phase 5 — [NLP & Transformers](phases/05-nlp-transformers.md)** · Tokenization, attention, BERT/GPT · _3–4 wks_
- **Phase 6 — [LLMs & Generative AI](phases/06-llms.md)** · Prompting, fine-tuning, evaluation · _3–4 wks_
- **Phase 7 — [AI Engineering: RAG & Vector DBs](phases/07-ai-engineering-rag.md)** · Embeddings, retrieval, RAG apps · _3–4 wks_
- **Phase 8 — [AI Agents & Agentic Systems](phases/08-agents.md)** · Tool use, orchestration, MCP · _3–4 wks_
- **Phase 9 — [MLOps & Production](phases/09-mlops-production.md)** · Serving, Docker, CI/CD, monitoring · _4–5 wks_
- **Phase 10 — [Portfolio, Specialization & Interview Prep](phases/10-career.md)** · Get hired · _ongoing_

### Visual path

```text
  FOUNDATIONS          CORE ML                AI / LLM STACK              SHIP
  ───────────          ───────                ──────────────              ────
  Phase 0 ─┐
  Programming         Phase 3                Phase 6                   Phase 9
           ├─► Phase 2 ─► Classical ML ─► …  LLMs ─► Phase 7 ─► Phase 8 ─► MLOps ─► Phase 10
  Phase 1 ─┘   Data        Phase 4           (RAG)    (Agents)            Get Hired 🎉
  Math/Stats              Deep Learning
                          Phase 5 (NLP/Transformers)

  Fast path (AI Engineer):  0 ─► 2 ─► 6 ─► 7 ─► 8 ─► 9 ─► 10   (skim 1, 3, 4, 5)
  Full path (ML Engineer):  0 ─► 1 ─► 2 ─► 3 ─► 4 ─► 5 ─► 6 ─► 9 ─► 10  (then 7, 8)
```

---

## 🛣️ Two ways to use this roadmap

### Path A — "I want to be an **AI Engineer**" (LLM apps, fastest to employable)
You build with existing models instead of training from scratch.
> **0 → 2 → 6 → 7 → 8 → 9 → 10** (skim 1, 3, 4, 5 for intuition)
> ~4–5 months. Best if you already code.

### Path B — "I want to be an **ML Engineer / Researcher**" (train & ship models)
You understand models deeply and can build them.
> **0 → 1 → 2 → 3 → 4 → 5 → 6 → 9 → 10** (then 7, 8 as needed)
> ~7–9 months. The complete foundation.

Not sure? Do **Path A** first to get momentum and a job, then backfill **Path B** depth on the side. See [`docs/which-path.md`](docs/which-path.md).

---

## 📅 Suggested weekly schedule (sustainable pace)

- **Mon–Tue** — New concepts (video/reading)
- **Wed–Thu** — Code along + exercises
- **Fri** — Build / extend the phase project
- **Sat** — Review, flashcards, write notes
- **Sun** — Rest or light reading

> **Rule:** never let a phase be 100% theory. Every phase ships a small project. Code beats notes.

---

## 📂 What's in this repo

```
.
├── README.md                ← you are here
├── phases/                  ← one file per phase: goals, checklist, resources, project
├── projects/PROJECTS.md     ← the portfolio projects, by difficulty
├── resources/RESOURCES.md   ← master list of best courses, books, channels, tools
├── interview/PREP.md        ← ML/AI interview prep (concepts + system design + behavioral)
├── docs/which-path.md       ← AI Engineer vs ML Engineer decision guide
└── progress.md              ← your personal progress tracker (check the boxes!)
```

---

## ✅ How to track progress

1. Fork / clone this repo.
2. Open [`progress.md`](progress.md) and check boxes as you complete each topic.
3. Commit your project work into `projects/` — that becomes your **portfolio**.
4. At the end you'll have a green progress file + a folder of real projects to show employers.

---

## 🧭 Guiding principles

1. **Build > watch.** A finished mediocre project teaches more than three perfect tutorials.
2. **Just-in-time math.** Don't grind all the math up front. Learn it when a model needs it.
3. **One model from scratch.** Implement at least one neural net and one transformer block by hand — once. Then use libraries forever.
4. **Ship in public.** Push every project to GitHub. Write a short README for each.
5. **Read papers early.** Even if you understand 30%. It compounds.

---

## 🚀 Start here

👉 **[Phase 0 — Programming Foundations](phases/00-foundations.md)**

> Already a strong Python dev? Take the [Phase 0 self-test](phases/00-foundations.md#self-test) — if you pass, skip to Phase 1 or 2.

---

*Roadmap maintained by [@ahfoysal](https://github.com/ahfoysal). PRs and suggestions welcome. ⭐ the repo if it helps.*
