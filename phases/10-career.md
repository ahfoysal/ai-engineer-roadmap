# Phase 10 — Portfolio, Specialization & Getting Hired

**Goal:** Turn your skills into a job. Build a portfolio, pick a specialization, and prepare for interviews — leveraging the SWE credibility you already have.
**Time:** Ongoing — start during Phase 6, intensify after Phase 9.

---

## 🎯 Outcomes
You have a public portfolio of deployed projects, a clear specialization, a resume/profile that leads with your production strength, and you can pass technical interviews. You know how to frame your transition so a hiring manager sees you as a *low-risk hire who already ships software* — not a junior who happens to know some ML.

## ✅ Checklist

### Portfolio (your strongest signal)
- [ ] 3–5 polished projects on GitHub, each with a clear README + live demo
- [ ] At least one **deployed** project with a live URL (not a notebook)
- [ ] At least one project that solves a *real* problem (yours or someone's)
- [ ] Clean commit history; pinned repos; CI badge + Dockerfile in your best repo
- [ ] Write up 2–3 projects as blog posts / LinkedIn posts
- [ ] (Bonus) One merged open-source contribution to an AI library

### Pick a specialization
- [ ] **LLM / GenAI Engineer** — RAG, agents, LLM apps (hottest, fastest hire for SWEs)
- [ ] **ML Engineer** — training, deployment, MLOps
- [ ] **Data Scientist** — analysis, experimentation, modeling
- [ ] **MLOps / Platform Engineer** — infra, scaling, reliability (huge SWE overlap)
- [ ] **Computer Vision** / **NLP** / **Recommender Systems** (domain depth)
- [ ] **Research Engineer** — papers, novel models (needs more math)

### Profile & applications
- [ ] Resume tuned to ML/AI (projects > coursework, metrics + impact, lead with production)
- [ ] LinkedIn & GitHub aligned with your target role and headline
- [ ] A 30-second "why I'm transitioning" story ready for interviews
- [ ] Network: AI communities, meetups, X, Discord, ex-colleagues
- [ ] Track applications; apply to roles slightly above your level

### Keep learning (the field moves fast)
- [ ] Follow papers ([arXiv](https://arxiv.org/list/cs.LG/recent), [Papers with Code](https://paperswithcode.com/))
- [ ] Newsletters/podcasts (The Batch, Latent Space, Import AI)
- [ ] Reproduce one new paper or model per quarter

---

## Portfolio strategy: ship software, not notebooks

**3–5 polished, deployed projects beat 20 tutorials.** Tutorials prove you can follow instructions; deployed projects prove you can build. Hiring managers skim — they want to click a live URL, see something work, and read clean code. Depth over breadth: one impressive RAG app you can speak to for 20 minutes outweighs ten half-finished Colab notebooks.

**This is exactly where your SWE background wins.** Most ML-curious candidates stop at a Jupyter notebook with great accuracy and no way to run it. You already know how to wrap a model in a service, containerize it, add CI, and put it behind a real URL. That gap *is* your edge — lean into it hard.

### What a great AI project README contains
- **One-line pitch + a screenshot or GIF** at the very top
- **Live demo link** and a "Try it" section (don't make them clone to see it work)
- **The problem** and *why* it matters
- **Architecture diagram** — model/LLM, data flow, retrieval, serving
- **How it works** — model choice, prompt/RAG strategy, key trade-offs you made
- **Results / evaluation** — metrics, latency, cost per request, before/after
- **Run locally** — `docker compose up` or a 3-line quickstart
- **Limitations & next steps** (signals engineering maturity)

### Ship *software*, not Jupyter
- **Deploy it** — a live URL (Hugging Face Spaces, Render, Fly.io, Railway, a cloud VM) is worth more than any accuracy number.
- **CI/CD** — a GitHub Actions workflow running tests/lint shows you treat ML like real software.
- **Docker** — reproducible environments. ML notoriously breaks across machines; a working `Dockerfile` quietly proves competence.
- **Tests** — even a few; evaluation harnesses and regression tests for prompts/models are gold.
- **A real UI or API** — Streamlit/Gradio for fast demos, FastAPI for a proper service.

### Turn projects into reach
- **Blog/LinkedIn posts** — write up *what you built, what broke, what you'd do differently*. The build-in-public loop compounds: posts attract recruiters, generate referrals, and double as interview talking points. One honest "here's how I cut my RAG latency 4×" post outperforms a dozen reposts.
- **Open-source contributions** — even small PRs (docs, bug fixes, an integration) to libraries like LangChain, LlamaIndex, Hugging Face `transformers`, vLLM, or a vector DB put your name in the ecosystem and give you a credible "I contribute to the tools I use" line.

---

## Specialization paths — pick one to go deep

You can't be everything. Pick a primary lane, build your portfolio toward it, and tune your resume to match. "Is this you?" for each:

- **LLM / GenAI Engineer** — *Is this you?* You like building products: RAG pipelines, agents, tool-use, evaluation, prompt and context engineering. You care more about shipping a useful LLM app than training models from scratch. **Fastest hire for an SWE** — it's mostly software engineering with an LLM in the loop, demand is enormous, and your app-building skills transfer almost directly.
- **ML Engineer** — *Is this you?* You enjoy the full lifecycle: data → training → deployment → monitoring. You want to own models in production, not just notebooks. A natural fit for SWEs who want depth in modeling without going full research.
- **Data Scientist** — *Is this you?* You love statistics, experimentation, and turning data into decisions (A/B tests, forecasting, analysis). More stats and communication, less systems work — the *least* aligned with a pure SWE background, so expect more new ground to cover.
- **MLOps / Platform Engineer** — *Is this you?* You like infra, pipelines, scaling, reliability, and developer experience. You'd rather build the platform that serves 100 models than tune one. **Huge SWE overlap** — if you came from backend/infra/DevOps, this can be your fastest path; you already speak Kubernetes, CI/CD, and observability.
- **CV / NLP / RecSys specialist** — *Is this you?* You want deep domain expertise in vision, language, or recommendations. Great for targeting specific industries (medical imaging, search, ads). Needs more domain-specific theory but pays for focus.
- **Research Engineer** — *Is this you?* You want to implement and push on novel architectures, reproduce papers, and work alongside researchers. **Needs the most math** (linear algebra, optimization, probability) and usually a strong publication or reproduction record. Slowest path from a pure SWE start.

**SWE shortcut:** the two fastest on-ramps from software engineering are **LLM/GenAI Engineer** and **MLOps/Platform** — both reward exactly the production skills you already have.

---

## Resume & profile tuning for AI/ML

Your resume is a positioning document, not a history. Reframe it for the role.

- **Lead with production strength.** Open with the thing few ML candidates have: "Built and shipped X to N users, owned it in production." That sentence does more than any course certificate.
- **Projects > coursework.** List 2–3 deployed projects with live links high on the page. A long list of courses signals "still learning"; a deployed app signals "already building."
- **Metrics & impact, always.** "Improved retrieval accuracy from 71% → 89%, cut p95 latency to 400ms, reduced cost/query 60%." Numbers convert. Quantify your *old* SWE work too (scale, uptime, traffic) — it proves you operate at production scale.
- **Translate your past.** "Backend engineer, 5 yrs" → "Built scalable services and data pipelines (the hard part of ML systems) — now applying them to ML." Don't hide your background; reframe it as the foundation.
- **GitHub ↔ LinkedIn ↔ resume alignment.** Same headline, same top projects, same target role. Pin your best repos. A recruiter who clicks through should see one consistent story. A headline like "Software Engineer → ML/LLM Engineer | Shipping production AI" works.
- **Network deliberately.** Referrals beat the resume pile. Reconnect with ex-colleagues now in ML, post your projects, show up in Discords/communities, and DM authors of tools you used. Most great ML roles are filled before they're widely posted.

### How to talk about your transition (SWE angle)
When asked "why the switch?", don't apologize for being new to ML. Frame it as a **strength compounding**, not a restart:

> "I've spent X years shipping production software — services, data pipelines, the on-call, the works. What I kept seeing is that the hard part of ML in the real world isn't the model, it's everything around it: serving, latency, cost, evaluation, reliability. That's the part I'm already good at, and I've spent the last [N months] going deep on the modeling side. So I'm not starting over — I'm bringing the production muscle most ML projects are missing."

This reframes "junior in ML" into "senior engineer who closes the gap teams struggle with." Back it with your deployed projects.

---

## 🎤 Interview preparation
See the dedicated guide: **[interview/PREP.md](../interview/PREP.md)** — covers ML concepts, coding, ML system design, take-homes, and behavioral. As a SWE you'll likely be *strong* on coding and system design and *softer* on ML theory and ML-specific system design — front-load your prep there. Don't neglect DS&A: some companies still test it, and it's the one area where you should already be comfortable.

## ⚠️ Pitfalls
- **Tutorial hell.** Endlessly consuming courses to feel "ready." You learn by building and shipping. Cap tutorials; start a real project this week.
- **No deployed projects.** Notebooks with great accuracy and no live URL read as "hasn't shipped." Always deploy at least one.
- **Undervaluing your SWE edge.** Trying to out-math the PhDs instead of out-shipping everyone. Your production skills are the differentiator — lead with them.
- **Applying too junior.** Don't reset to entry-level pay/title. You're an experienced engineer changing focus; target mid/senior roles and let projects carry the ML credibility.
- **Breadth over depth.** Ten shallow projects across every framework beat one polished, deployed, well-documented app. They don't.
- **A messy profile.** Stale LinkedIn, no pinned repos, no demo links. Recruiters bounce in seconds.

## 🔑 Key terms & quick tips
- **Portfolio piece** — a deployed project you can defend for 20 minutes, end to end.
- **Build in public** — ship + write about it; the loop attracts opportunities.
- **Production-grade** — CI, Docker, tests, monitoring, a live URL. Your home turf.
- **Specialization** — your primary lane; everything else is supporting depth.
- **Referral** — the highest-yield application channel; cultivate your network now.
- *Quick tip:* one polished, deployed, written-up project per month for 4 months → a portfolio that lands interviews.
- *Quick tip:* if you can't deploy it, you can't demo it; if you can't demo it, it barely counts.

## 📚 Best resources
- **Interview** — [*Machine Learning Interviews* by Chip Huyen (free book)](https://huyenchip.com/ml-interviews-book/) · [*Designing Machine Learning Systems* (Chip Huyen)](https://www.oreilly.com/library/view/designing-machine-learning/9781098107956/)
- **Deployment** — [Hugging Face Spaces](https://huggingface.co/spaces) · [Render](https://render.com/) · [Fly.io](https://fly.io/) for putting projects behind a live URL
- **Portfolio inspiration** — browse top AI engineers' GitHub profiles and the [Papers with Code](https://paperswithcode.com/) leaderboards for project ideas
- **Practice** — [LeetCode](https://leetcode.com/) (some companies still test DS&A — play to this strength) · mock interviews
- **Stay current** — [The Batch](https://www.deeplearning.ai/the-batch/) · [Latent Space](https://www.latent.space/) · [Import AI](https://importai.net/)

## 🛠️ Capstone project
**Build one impressive, end-to-end, deployed AI product** that becomes the centerpiece of your portfolio — and the proof that you ship software, not notebooks.

**Acceptance criteria**
- [ ] Solves a *real* problem with a real model or LLM system (RAG or an agent)
- [ ] Has a clean UI and/or a documented API
- [ ] **Deployed** to the cloud with a working live URL anyone can try
- [ ] Containerized (`Dockerfile`) and runs locally with a one-command quickstart
- [ ] CI pipeline (tests/lint) green on the repo
- [ ] Includes evaluation: metrics, latency, and cost per request
- [ ] Has basic monitoring/logging in production
- [ ] Ships with a great README (pitch, demo, architecture, results, limitations)
- [ ] Written up as a blog/LinkedIn post you can link from your resume

🎉 **You made it.** Now go build things and ship them. The field rewards builders — and you already know how to build.

⬅️ Back to [README](../README.md)
