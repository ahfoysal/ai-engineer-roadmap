# Phase 1 — Math & Statistics for ML

**Goal:** Understand the math *behind* models well enough to reason about them — not to become a mathematician.
**Time:** 3–4 weeks. **Learn just-in-time:** skim now, return when a model uses a concept.

---

## 🎯 Outcomes
You can read an ML paper's notation, understand what a gradient is, interpret probability/statistics, and know why models work.

## ✅ Checklist

### Linear algebra (most important)
- [ ] Vectors, matrices, tensors
- [ ] Matrix multiplication, transpose, identity, inverse
- [ ] Dot product & cosine similarity (core to embeddings!)
- [ ] Eigenvalues/eigenvectors (intuition), PCA
- [ ] Norms (L1, L2)

### Calculus
- [ ] Derivatives, partial derivatives
- [ ] The gradient & chain rule (this *is* backpropagation)
- [ ] Gradient descent intuition (going downhill)

### Probability & statistics
- [ ] Mean, median, variance, standard deviation
- [ ] Probability distributions: normal, Bernoulli, binomial
- [ ] Conditional probability & Bayes' theorem
- [ ] Expectation, sampling, the law of large numbers
- [ ] Correlation vs causation
- [ ] Hypothesis testing & p-values (basics)
- [ ] Maximum likelihood estimation (intuition)

## 📚 Best resources
- **Visual intuition** — [3Blue1Brown: Essence of Linear Algebra](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab) + [Essence of Calculus](https://www.youtube.com/playlist?list=PLZHQObOWTQDMsr9K-rj53DwVRMYO3t5Yr) **(do these — they're the best)**
- **Course** — [Khan Academy: Linear Algebra / Statistics](https://www.khanacademy.org/math) (free)
- **ML-focused** — [Mathematics for Machine Learning (book, free PDF)](https://mml-book.github.io/) · [Imperial College "Maths for ML" (Coursera)](https://www.coursera.org/specializations/mathematics-machine-learning)
- **Stats** — [StatQuest with Josh Starmer (YouTube)](https://www.youtube.com/c/joshstarmer) — *legendary for intuition*

## 🛠️ Phase project
**Implement gradient descent from scratch** in NumPy to fit a line to data (linear regression). Plot the loss going down over iterations. No scikit-learn allowed.

> ⚠️ Don't perfect this phase. 70% intuition is enough to start building. You'll deepen it in Phase 4.

➡️ Next: [Phase 2 — Data Wrangling & Analysis](02-data.md)
