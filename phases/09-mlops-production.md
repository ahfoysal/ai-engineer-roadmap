# Phase 9 — MLOps & Production

**Goal:** Ship AI systems that survive contact with real users — deployed, monitored, reproducible, and cost-controlled. This is what separates a hobbyist from an engineer.
**Time:** 4–5 weeks.

---

## 🎯 Outcomes
You can take a model/AI app from notebook to a deployed, monitored, maintainable production service.

## ✅ Checklist

### Serving models & apps
- [ ] Build APIs with **[FastAPI](https://fastapi.tiangolo.com/)**
- [ ] Serve ML models (REST endpoints, batch vs real-time)
- [ ] Frontends/demos: [Streamlit](https://streamlit.io/) / [Gradio](https://www.gradio.app/)
- [ ] LLM serving & inference (vLLM, TGI) — awareness

### Packaging & deployment
- [ ] **Docker** (containerize your app)
- [ ] Environment & dependency management (`uv`, `requirements`, lockfiles)
- [ ] Deploy to cloud: AWS / GCP / Azure, or [Modal](https://modal.com/) / [Hugging Face Spaces](https://huggingface.co/spaces) / Railway
- [ ] GPUs in the cloud, serverless inference
- [ ] Secrets & config management

### MLOps practices
- [ ] **Experiment tracking** ([Weights & Biases](https://wandb.ai/), [MLflow](https://mlflow.org/))
- [ ] Model & data versioning ([DVC](https://dvc.org/))
- [ ] **CI/CD** (GitHub Actions) for ML
- [ ] Model registry & reproducibility
- [ ] Feature stores (awareness)

### Monitoring & reliability (LLMOps)
- [ ] Logging & tracing requests
- [ ] **Monitoring drift, latency, cost, quality**
- [ ] Observability for LLM apps ([Langfuse](https://langfuse.com/), [LangSmith](https://www.langchain.com/langsmith))
- [ ] Caching (semantic cache to cut cost)
- [ ] Rate limiting, retries, fallbacks
- [ ] A/B testing & gradual rollouts

### Engineering hygiene
- [ ] Testing (pytest), linting, type checking
- [ ] Writing good READMEs & docs
- [ ] Security: API keys, PII, prompt-injection defense

## 📚 Best resources
- **Course** — [Made With ML by Goku Mohandas (free, gold standard)](https://madewithml.com/) · [Full Stack Deep Learning](https://fullstackdeeplearning.com/)
- **roadmap.sh** — [MLOps Roadmap](https://roadmap.sh/mlops)
- **Docker/FastAPI** — [FastAPI docs](https://fastapi.tiangolo.com/) · [Docker get started](https://docs.docker.com/get-started/)
- **Book** — *Designing Machine Learning Systems* by Chip Huyen **(essential)** · *AI Engineering* by Chip Huyen (2025)

## 🛠️ Phase project
**Productionize one earlier project.** Take your RAG app or agent and: containerize it with Docker, build a FastAPI backend, add logging + monitoring + caching, deploy it to the cloud with a public URL, and set up GitHub Actions CI. This is the project that gets you hired.

➡️ Next: [Phase 10 — Portfolio, Specialization & Interview Prep](10-career.md)
