# Phase 1 — Math & Statistics for ML

**Goal:** Understand the math *behind* models well enough to reason about them — not to become a mathematician.
**Time:** 3–4 weeks. **Learn just-in-time:** skim now, return when a model actually uses a concept.

---

> **You do not need a math degree.** You need to read notation without panicking and have intuition for *why* models work. As a working engineer you already think in vectors of data, functions, and feedback loops — that's 80% of the mental model. The rest is vocabulary. Build *intuition first*, reach for rigor only when a real problem demands it.

## 🎯 Outcomes
You can read an ML paper's notation, explain what a gradient is and why we follow it, interpret a probability or a confidence interval, and articulate *why* a model learns. When you see `θ ← θ − α∇J(θ)` you think "nudge the weights downhill," not "I'm lost."

## ✅ Checklist

### Linear algebra (most important — this is the language of ML)
- [ ] Vectors, matrices, tensors — and why data is always shaped like this
- [ ] Matrix multiplication, transpose, identity, inverse
- [ ] Dot product & cosine similarity (the heart of embeddings & search!)
- [ ] Norms (L1, L2) — measuring size/distance, and why regularization uses them
- [ ] Eigenvalues/eigenvectors (intuition only) → PCA & dimensionality reduction
- [ ] Broadcasting & matrix shapes in NumPy (debugging shape errors is a daily skill)

### Calculus
- [ ] Derivatives — slope, rate of change
- [ ] Partial derivatives — slope in one direction when many inputs vary
- [ ] The gradient & chain rule (this *is* backpropagation)
- [ ] Gradient descent intuition (rolling downhill to the minimum)
- [ ] Learning rate intuition (step size: too big overshoots, too small crawls)

### Probability & statistics
- [ ] Mean, median, variance, standard deviation
- [ ] Probability distributions: normal, Bernoulli, binomial
- [ ] Conditional probability & Bayes' theorem
- [ ] Expectation, sampling, the law of large numbers
- [ ] Correlation vs causation (the trap behind half of bad ML claims)
- [ ] Hypothesis testing & p-values (basics — enough to read an A/B test)
- [ ] Maximum likelihood estimation (intuition: "what parameters make my data most plausible?")

---

## Linear algebra — the language models speak

Almost everything in ML is "multiply a big grid of numbers by another big grid of numbers." That's it. Get comfortable here and the rest gets easier.

- **Vectors / matrices / tensors.** A vector is a list of numbers (one example: `[1.2, -0.4, 3.0]`). A matrix is a grid (a batch of examples, one per row). A tensor is just "n-dimensional array" — a batch of images is a 4D tensor `(batch, height, width, channels)`. You already use these: they're arrays.
  - *Where in ML:* every input, weight, and activation is one of these.
- **Matrix multiplication.** A neural network layer is literally `output = inputs · weights + bias`. Stacking layers = chaining matrix multiplies. The "shapes must line up" rule (`(m×n) · (n×p) = (m×p)`) is the #1 source of beginner bugs — learn to read shapes.
  - *Where in ML:* every forward pass through a layer.
- **Dot product & cosine similarity.** The dot product `a · b` sums `a[i]*b[i]`. Cosine similarity is the dot product of *normalized* vectors — it measures the **angle** between them, ignoring length. Two vectors pointing the same way → ~1; orthogonal → 0; opposite → −1.
  - *Where in ML:* **this is how embeddings and vector search work.** "Find similar documents/images/users" = "find vectors with high cosine similarity." If you only deeply learn one thing in this phase, learn this.
- **Norms (L1, L2).** A norm measures a vector's size. **L2** = ordinary straight-line length (`√Σx²`). **L1** = sum of absolute values (`Σ|x|`). Distance between two points is the norm of their difference.
  - *Where in ML:* loss functions (MSE is an L2 distance), and **regularization** — L2 (ridge) shrinks weights smoothly, L1 (lasso) drives some weights to exactly zero (feature selection).
- **Eigenvalues / eigenvectors → PCA.** Don't grind the algebra. The intuition: any dataset has directions in which it varies the most. PCA finds those directions (the top eigenvectors of the covariance matrix) and lets you keep the few that capture most of the information, dropping the rest.
  - *Where in ML:* dimensionality reduction, compression, visualization, de-noising features.

## Calculus — how models learn

You need calculus for *one reason*: training a model means minimizing a loss, and we minimize by following slopes downhill. Everything below serves that.

- **Derivative.** The slope of a function — "if I nudge the input a little, how much does the output change, and in which direction?"
- **Partial derivative.** A model has millions of parameters. A partial derivative answers "how does the loss change if I wiggle *this one* parameter, holding the rest fixed?"
- **Gradient (∇).** Just the vector of all those partial derivatives — it points in the direction of **steepest increase** of the loss. So the *negative* gradient points straight downhill toward lower loss.
- **Chain rule = backpropagation.** A network is functions wrapped in functions wrapped in functions. The chain rule says: to get the derivative of the whole stack, multiply the derivatives layer by layer, working backward from the loss. **That's all backprop is** — the chain rule applied efficiently across a computation graph. Frameworks (PyTorch, JAX) do this for you with autograd; you just need to know *what* they're computing and why.
  - *Where in ML:* every training step of every neural network.
- **Gradient descent (rolling downhill).** Imagine a ball on a hilly loss landscape. At each step: measure the slope (gradient), take a small step downhill, repeat. The **learning rate** `α` is your step size — too large and you bounce out of the valley, too small and training takes forever. Update rule: `θ ← θ − α∇J(θ)`. Read it as "move every weight a little bit against the gradient."
  - *Where in ML:* the core training loop. SGD, Adam, etc. are all flavors of this.

## Probability & statistics — reasoning under uncertainty

Models output probabilities and you evaluate them statistically. You don't need measure theory; you need to reason about uncertainty and not fool yourself.

- **Mean / variance / std.** Center and spread of data. Variance is "average squared distance from the mean"; std is its square root (same units as the data). You'll *normalize* features using these constantly.
- **Distributions.**
  - **Normal (Gaussian)** — the bell curve; shows up everywhere (noise, weight initialization, the "68/95/99.7" rule).
  - **Bernoulli** — a single yes/no event with probability `p` (one coin flip). Binary classifiers model this.
  - **Binomial** — count of successes over `n` Bernoulli trials.
  - *Where in ML:* loss functions and model outputs assume distributions (e.g. cross-entropy assumes a Bernoulli/categorical output).
- **Conditional probability & Bayes' theorem.** `P(A|B)` = probability of A *given* B is known. Bayes flips it: `P(A|B) = P(B|A)·P(A) / P(B)`. Intuition: update your belief about a cause given observed evidence.
  - *Where in ML:* naive Bayes classifiers, spam filters, and the whole Bayesian/uncertainty-estimation mindset.
- **Expectation & sampling.** Expectation = the long-run average value (a probability-weighted mean). The **law of large numbers** says sample averages converge to the true expectation as you collect more data — which is *why* training on more data works.
  - *Where in ML:* loss = expected error; mini-batches are samples approximating it.
- **Correlation vs causation.** Two variables moving together does **not** mean one causes the other. This is the single most common reasoning error in applied ML — a feature can predict an outcome without causing it, and that breaks the moment the world shifts.
- **Hypothesis testing & p-values (basics).** A p-value is "the probability of seeing a result this extreme if nothing real were going on (the null hypothesis)." Small p (e.g. < 0.05) = "probably not just noise." Enough to read an A/B test result without being misled — and to know p-hacking is real.
- **Maximum likelihood estimation (MLE).** Intuition: pick the model parameters that make your observed data **most probable**. Minimizing common losses (MSE, cross-entropy) is mathematically equivalent to maximizing likelihood — so MLE is the "why" behind the loss functions you'll use.

---

## 🤔 How much do I *really* need? (map to your track)

Tune your depth to where you're headed. You can always come back.

- **AI Engineer / LLM app builder** (using APIs, RAG, agents, prompt pipelines): you need **less**.
  - *Must have:* vectors, dot product & **cosine similarity** (embeddings/RAG live here), basic probability, mean/variance, correlation≠causation.
  - *Nice to have:* gentle gradient-descent intuition. You can mostly skip eigenvectors, MLE proofs, and hand-derived backprop.
- **ML Engineer / Data Scientist** (training, fine-tuning, custom models): you need **more**.
  - *Must have:* all of the above **plus** the gradient/chain-rule story, gradient descent & learning rates, distributions, MLE intuition, PCA, and comfort reading paper notation.
  - *Go deeper later (Phase 4):* optimization details, regularization math, probabilistic modeling.
- **Either way:** depth is *just-in-time*. Aim for ~70% now; you'll cement the rest by *using* it on real models.

## 🔑 Key terms (quick glossary)
- **Scalar / vector / matrix / tensor** — a number / a list / a grid / an n-dimensional array.
- **Dot product** — element-wise multiply then sum; measures alignment of two vectors.
- **Cosine similarity** — dot product of unit vectors; similarity by angle, used in embedding search.
- **Norm** — the "length" of a vector (L1 = sum of abs, L2 = straight-line length).
- **Gradient (∇)** — vector of partial derivatives; points uphill, so we step the opposite way.
- **Backpropagation** — the chain rule applied through a network to get gradients.
- **Learning rate (α)** — step size in gradient descent.
- **Loss / cost function** — the number we're trying to minimize (how wrong the model is).
- **Distribution** — how probability is spread over possible values (e.g. normal, Bernoulli).
- **Bayes' theorem** — rule for updating a belief given new evidence.
- **Expectation** — long-run probability-weighted average.
- **MLE** — choosing parameters that make the observed data most probable.
- **PCA** — finding the directions of greatest variance to reduce dimensions.

## ⚠️ Pitfalls
- **Over-grinding the math up front.** Don't spend 3 months on proofs before touching a model. You'll forget unused theorems and burn out. Learn enough to start, then deepen by need.
- **Skipping it entirely.** The opposite failure. Without *any* intuition, models stay magic, errors stay mysterious, and you can't debug a training run or read a paper. Aim for the middle: solid intuition, light rigor.
- **Memorizing formulas you never run.** Implement things instead — a formula you've coded once sticks far better than one you've highlighted ten times.
- **Confusing correlation with causation** in your own analyses. Stay paranoid about this.
- **Fighting shape errors blindly.** When NumPy/PyTorch throws a shape mismatch, *read the shapes* — linear algebra is telling you exactly what's wrong.

## 📚 Best resources
- **Visual intuition (do these first — they're the best)** — [3Blue1Brown: Essence of Linear Algebra](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab) + [Essence of Calculus](https://www.youtube.com/playlist?list=PLZHQObOWTQDMsr9K-rj53DwVRMYO3t5Yr). Watch these even if you "did calculus in college" — the geometric intuition is the missing piece.
- **Stats intuition** — [StatQuest with Josh Starmer (YouTube)](https://www.youtube.com/c/joshstarmer) — *legendary* for making distributions, p-values, and PCA click.
- **Course / drills** — [Khan Academy: Linear Algebra, Calculus & Statistics](https://www.khanacademy.org/math) (free, practice problems).
- **ML-focused, when you want rigor** — [Mathematics for Machine Learning (free book/PDF)](https://mml-book.github.io/) · [Imperial College "Mathematics for Machine Learning" (Coursera specialization)](https://www.coursera.org/specializations/mathematics-machine-learning).
- **Reference** — keep [NumPy's docs](https://numpy.org/doc/stable/) open; you'll learn the linear algebra *by doing it in code*.

## 🛠️ Phase project
**Implement gradient descent + linear regression from scratch in NumPy.** No scikit-learn.

1. Generate noisy linear data: `y = 3x + 2 + noise`.
2. Define the model `ŷ = wx + b` and the **MSE loss** (this is an L2 distance — connect it back!).
3. Derive the gradients of the loss w.r.t. `w` and `b` by hand (chain rule practice), then code them.
4. Run the update loop: `w ← w − α·∂L/∂w`, `b ← b − α·∂L/∂b`.
5. **Plot the loss curve** over iterations (watch it roll downhill) and plot the fitted line over the data.
6. *Stretch:* try a too-large and a too-small learning rate and watch what happens. Then vectorize it with matrix operations.

You'll touch nearly every concept in this phase — vectors, dot products, gradients, the chain rule, MSE, and learning rates — in ~40 lines of code. That's the payoff.

> ⚠️ Don't perfect this phase. 70% intuition is enough to start building. You'll deepen it naturally in Phase 4 when models force you to.

➡️ Next: [Phase 2 — Data Wrangling & Analysis](02-data.md)
