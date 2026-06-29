# 🎤 AI / ML Interview Preparation

ML/AI interviews typically have 4–5 components. Prepare each. Don't grind LeetCode at the expense of ML depth and projects.

## 1. ML / DL concepts (the core)
Be able to explain clearly and with a whiteboard:
- [ ] Bias-variance tradeoff; over/underfitting; how to fix each
- [ ] Regularization (L1 vs L2) and what they do
- [ ] How gradient descent & backpropagation work
- [ ] Precision/recall/F1/ROC-AUC — and when accuracy misleads
- [ ] Cross-validation; train/val/test discipline; data leakage
- [ ] How a transformer / self-attention works
- [ ] Embeddings & cosine similarity
- [ ] Prompting vs RAG vs fine-tuning — trade-offs
- [ ] How RAG works end-to-end and how to improve retrieval
- [ ] What makes an LLM hallucinate and how to reduce it
- [ ] Evaluation: how do you know your model/LLM is good?

## 2. Coding
- [ ] Python data manipulation (Pandas/NumPy) live
- [ ] Implement a metric or algorithm from scratch (e.g. k-means, train loop)
- [ ] Some companies: DS&A (arrays, hashmaps, two-pointers) — [LeetCode](https://leetcode.com/) easy/medium
- [ ] Debug/extend an ML notebook

## 3. ML system design (senior signal)
Practice designing end-to-end systems out loud:
- [ ] "Design a recommendation system / spam filter / search ranking"
- [ ] "Design a RAG system for company docs at scale"
- [ ] "Design an LLM agent for customer support"
- Framework: clarify requirements → data → features → model → eval → serving → monitoring → iteration
- Read: *Designing ML Systems* (Huyen) + [ML system design primer]

## 4. Take-home / project deep-dive
- [ ] Be ready to explain **every decision** in your portfolio projects
- [ ] Know your projects' metrics, trade-offs, and what you'd improve
- [ ] Practice presenting a project in 5 minutes

## 5. Behavioral
- [ ] STAR stories: a hard bug, a project you shipped, a conflict, a failure
- [ ] Why AI/ML? Why this company?
- [ ] Questions to ask them (team, stack, how they use AI)

## 📚 Resources
- [*Machine Learning Interviews* — Chip Huyen (free)](https://huyenchip.com/ml-interviews-book/)
- [*Designing Machine Learning Systems* — Chip Huyen](https://www.oreilly.com/library/view/designing-machine-learning/9781098107956/)
- Mock interviews with peers; record yourself answering concept questions

## 💡 Tips
- **Projects > everything.** A deployed, well-explained project beats a perfect LeetCode record for AI roles.
- **Show, don't tell.** Bring metrics and demos.
- **It's OK to say "I'd look that up."** Reasoning > memorization.
- Tailor prep to the role: GenAI roles → RAG/agents/prompting; ML roles → modeling/MLOps.
