# Phase 3 — Classical Machine Learning

**Goal:** Master the core ML algorithms and the workflow of training/evaluating models with scikit-learn.
**Time:** 4–5 weeks. **This is the heart of being an ML engineer.**

---

## 🎯 Outcomes
You can frame a problem as supervised/unsupervised, pick an algorithm, train it, evaluate it honestly, and avoid overfitting. Just as important: you can spot the silent mistakes (leakage, wrong metric, no baseline) that make a model *look* good in a notebook and fail in production.

## ✅ Checklist

### Core concepts
- [ ] Supervised vs unsupervised vs reinforcement learning
- [ ] Features, labels, training/validation/test split
- [ ] Overfitting vs underfitting, bias-variance tradeoff
- [ ] Cross-validation (k-fold, stratified)
- [ ] Feature scaling (standardization, normalization)
- [ ] Feature engineering & encoding (one-hot, label, target)
- [ ] Regularization (L1/Lasso, L2/Ridge)
- [ ] The full ML pipeline (`sklearn.Pipeline`) and **why you fit only on train**
- [ ] Set a baseline before any "real" model

### Supervised — regression
- [ ] Linear regression
- [ ] Polynomial regression
- [ ] Regularized linear (Ridge, Lasso, ElasticNet)

### Supervised — classification
- [ ] Logistic regression
- [ ] k-Nearest Neighbors (kNN)
- [ ] Decision trees
- [ ] Random forests
- [ ] Gradient boosting: **XGBoost / LightGBM** (wins most tabular competitions)
- [ ] Support Vector Machines (SVM)
- [ ] Naive Bayes

### Unsupervised
- [ ] k-Means clustering
- [ ] Hierarchical clustering
- [ ] PCA (dimensionality reduction)
- [ ] DBSCAN

### Evaluation (do not skip)
- [ ] Regression: MAE, MSE, RMSE, R²
- [ ] Classification: accuracy, **precision, recall, F1**, ROC-AUC
- [ ] Confusion matrix
- [ ] Why accuracy lies on imbalanced data
- [ ] Hyperparameter tuning (GridSearch, RandomSearch)

---

## 🧠 The mental model

As an SWE, you write the rules. In ML, you give the machine **examples** and it infers the rules. Your job shifts from "implement the logic" to "shape the data, pick the algorithm, and measure honestly." Most of the difficulty is in those last two words — *measure honestly*. The code is easy; not fooling yourself is hard.

A model is just a function `f(X) → y` whose parameters are *learned* by minimizing some error over training data. Everything below is about (a) how that function is shaped and (b) whether it actually generalizes to data it has never seen.

### Supervised vs unsupervised
- **Supervised** — you have labels (the "answer" for each row). Two sub-types: **regression** (predict a number, e.g. house price) and **classification** (predict a category, e.g. spam/not-spam). This is ~90% of business ML.
- **Unsupervised** — no labels. You find structure: clusters of similar rows, or a lower-dimensional view of the data. Used for segmentation, anomaly detection, compression.
- **Reinforcement** — an agent learns by acting and getting rewards. Powerful but niche; ignore it for now.

### Features and labels
- **Features (X)** — the input columns (square footage, age, num_bedrooms). A row is one example.
- **Label / target (y)** — what you're predicting. Only supervised learning has one.
- **Feature engineering** — turning raw data into features the model can use (e.g. `price_per_sqft` from `price` and `sqft`). This is usually where the biggest wins come from — far more than swapping algorithms.

### Train / validation / test
Split your data into three buckets and **never let them touch**:
- **Train** — the model learns parameters here.
- **Validation** — you tune hyperparameters and compare models here.
- **Test** — touched *once*, at the very end, to estimate real-world performance.

The whole point is to simulate "data the model has never seen." A typical split is 60/20/20, or 80/20 with cross-validation replacing the separate validation set.

### Overfitting vs underfitting
- **Underfitting** — model is too simple; it misses real patterns. High error on *both* train and test. (e.g. fitting a straight line to a curve.)
- **Overfitting** — model memorizes the training data, including its noise. Low train error, high test error. It learned the answer key, not the subject.
- The tell-tale sign of overfitting: a big gap between train score and validation score.

### Bias-variance tradeoff (intuitively)
Every model's error splits into two competing parts:
- **Bias** — error from wrong assumptions / being too simple. High bias → underfitting.
- **Variance** — error from being too sensitive to the specific training sample. High variance → overfitting.
Simple models (linear regression) are high-bias/low-variance. Flexible models (deep trees) are low-bias/high-variance. The art is finding the sweet spot — usually by adding flexibility *and* then reining it in with regularization or more data. Think of it as a dial: turn toward complexity and you reduce bias but risk variance, and vice-versa.

### Cross-validation
A single train/val split is noisy — you might get lucky or unlucky. **k-fold CV** splits the data into k parts, trains on k−1 and validates on the held-out part, and rotates k times. You average the k scores for a stable estimate. Use **stratified** k-fold for classification so each fold keeps the same class balance. Default to k=5.

### Feature scaling
Many algorithms care about the *magnitude* of features. If `income` is in the tens of thousands and `age` is under 100, distance- and gradient-based models will be dominated by income. Fix it:
- **Standardization** (`StandardScaler`) — subtract mean, divide by std → mean 0, std 1. The usual default.
- **Normalization** (`MinMaxScaler`) — squash to [0, 1].
- **Who needs it:** kNN, SVM, k-means, PCA, and any gradient-descent model. **Who doesn't:** tree-based models (trees split on thresholds, scale-invariant).

### Encoding categorical features
Models eat numbers, not strings. Convert categories:
- **One-hot** — one binary column per category. Safe default for low-cardinality features (`color`: red/green/blue).
- **Label/ordinal** — map categories to integers. Only valid when there's a real order (low/med/high), otherwise the model invents a fake ordering.
- **Target encoding** — replace a category with the mean target for that category. Powerful for high-cardinality features (zip codes) but a **classic leakage trap** — compute it inside cross-validation folds, never on the full dataset.

### Regularization (L1 / L2)
Regularization penalizes large model weights to fight overfitting:
- **L2 / Ridge** — penalizes the sum of squared weights. Shrinks weights smoothly toward zero; keeps all features. Good default.
- **L1 / Lasso** — penalizes the sum of absolute weights. Drives some weights *exactly* to zero → automatic feature selection. Good when you suspect many features are useless.
- **ElasticNet** — a blend of both.
The strength is a hyperparameter (`alpha`, or `C` = 1/strength in logistic regression / SVM). More regularization → simpler model → more bias, less variance.

### The Pipeline + why you fit on train only (data leakage)
A `Pipeline` chains preprocessing and the model into one object. This isn't just tidiness — it's the single best defense against **data leakage**.

> **Leakage** = information from the test set (or the future) sneaking into training. The model looks brilliant in your notebook, then face-plants in production.

The canonical mistake: you call `scaler.fit(X)` on the *whole* dataset before splitting. Now the scaler's mean/std were computed using test rows — your test set has secretly informed training. A `Pipeline` makes this almost impossible: when you call `pipe.fit(X_train)`, every step's `fit` sees only the training fold. During cross-validation, sklearn refits the *entire* pipeline on each fold automatically. **Rule: any step that *learns* from data (scalers, encoders, imputers) must be fit on train only.**

---

## 🤖 Algorithms — intuition, when to use, pros/cons

### Supervised — regression & linear models
- **Linear regression** — fits a straight line/hyperplane minimizing squared error. *Use when* the relationship is roughly linear and you want an interpretable baseline. *Pros:* fast, interpretable (coefficients = effect size). *Cons:* underfits non-linear data; sensitive to outliers.
- **Logistic regression** — despite the name, it's *classification*. Runs a linear combo through a sigmoid to output a probability. *Use as* your go-to classification baseline. *Pros:* fast, probabilistic, interpretable. *Cons:* only learns linear decision boundaries.

### Supervised — classification
- **k-Nearest Neighbors (kNN)** — to classify a point, look at its k closest neighbors and take a vote. No training, all the work happens at predict time. *Use for* small datasets and quick baselines. *Pros:* dead simple, no assumptions. *Cons:* slow at scale, needs scaling, dies in high dimensions ("curse of dimensionality").
- **Decision trees** — a flowchart of if/else splits chosen to best separate the target. *Use when* you want interpretability. *Pros:* readable, handles non-linearity, no scaling needed. *Cons:* a single tree overfits wildly — rarely used alone.
- **Random forests** — train many decision trees on random subsets of rows and features, then average them. *Use as* a strong, low-effort default that just works. *Pros:* robust, hard to overfit, minimal tuning, gives feature importances. *Cons:* less interpretable than one tree; larger models.
- **Gradient boosting (XGBoost / LightGBM)** — build trees *sequentially*, each one correcting the previous trees' mistakes. **This wins most tabular competitions and is the default winner on structured/tabular data.** *Pros:* state-of-the-art accuracy on tables, handles mixed feature types. *Cons:* more hyperparameters to tune, can overfit if you let it. **If you remember one algorithm for tabular data, make it this.** LightGBM is faster on big data; XGBoost is the battle-tested classic.
- **Support Vector Machines (SVM)** — find the boundary with the widest margin between classes; the "kernel trick" lets it carve non-linear boundaries. *Use for* small/medium datasets with clear separation. *Pros:* powerful in high dimensions, effective with clear margins. *Cons:* slow on large data, needs scaling, hard to interpret, fiddly to tune.
- **Naive Bayes** — applies Bayes' theorem assuming features are independent (the "naive" part). *Use for* text classification (spam, sentiment). *Pros:* extremely fast, works with little data and tons of features. *Cons:* the independence assumption is usually false, so probabilities are poorly calibrated.

### Unsupervised
- **k-Means** — partition data into k clusters by minimizing distance to cluster centers. *Use for* customer/segment grouping. *Pros:* fast, simple. *Cons:* you must pick k upfront (use the "elbow" or silhouette score), assumes round clusters, needs scaling.
- **Hierarchical clustering** — build a tree (dendrogram) of nested clusters; cut it at any level. *Use when* you don't know k and want to *see* the cluster structure. *Pros:* no preset k, interpretable dendrogram. *Cons:* slow ‑ O(n²) or worse, doesn't scale to large n.
- **DBSCAN** — clusters by density; points in sparse regions are labeled noise. *Use for* arbitrary-shaped clusters and outlier/anomaly detection. *Pros:* finds k itself, handles weird shapes, flags outliers. *Cons:* struggles with varying densities; sensitive to its `eps`/`min_samples` params.
- **PCA** — projects data onto the directions of maximum variance to reduce dimensions. *Use for* visualization, speeding up models, killing multicollinearity. *Pros:* compresses features, denoises. *Cons:* components aren't interpretable; it's linear; **always scale first**.

---

## 📊 Evaluation in depth

Picking the right metric matters more than picking the right algorithm. A model is only as good as the number you chose to optimize.

### Regression metrics
- **MAE** (mean absolute error) — average absolute miss, in the target's units. Robust to outliers, easy to explain.
- **MSE** (mean squared error) — squares errors, so it punishes big misses hard. Good when large errors are especially bad.
- **RMSE** — √MSE, back in the target's units. The most common reporting metric.
- **R²** — fraction of variance explained (1.0 = perfect, 0 = no better than predicting the mean, negative = worse than the mean). Great for "is this model even useful?"

### Classification metrics
Start with the **confusion matrix** — counts of true/false positives/negatives. Everything else is derived from it.
- **Accuracy** — % correct. Fine *only* when classes are balanced.
- **Precision** — of the things you flagged positive, how many really were? (Cost of false alarms — e.g. don't block legit transactions.)
- **Recall / sensitivity** — of the actual positives, how many did you catch? (Cost of misses — e.g. don't let cancer go undetected.)
- **F1** — harmonic mean of precision and recall. Use when you need balance and classes are imbalanced.
- **ROC-AUC** — probability the model ranks a random positive above a random negative, across all thresholds. Threshold-independent; 0.5 = random, 1.0 = perfect.

There's a real **precision/recall tradeoff** — push the decision threshold to catch more positives (↑recall) and you'll flag more false alarms (↓precision). The "right" balance is a *business* decision, not a math one.

### Why accuracy lies on imbalanced data
Suppose 1% of transactions are fraud. A model that predicts "not fraud" for *everything* scores **99% accuracy** — and is completely useless: it catches zero fraud. Accuracy rewarded the dumb majority-class guess. On imbalanced problems, reach for **precision, recall, F1, ROC-AUC**, or PR-AUC instead — and always compare against a baseline.

### Hyperparameter tuning
**Parameters** are learned (the weights). **Hyperparameters** are knobs *you* set (tree depth, k, regularization strength).
- **Grid search** — try every combination in a grid. Exhaustive but explodes combinatorially.
- **Random search** — sample random combinations. Usually finds near-best settings far faster — prefer it when the grid is large.
- Tune using **cross-validation on the train set** (`GridSearchCV` / `RandomizedSearchCV`), then evaluate the winner *once* on the untouched test set.

---

## 🧪 Code you should be able to write

A leakage-safe pipeline with mixed feature types, trained and scored:

```python
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score, classification_report

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=42
)

pre = ColumnTransformer([
    ("num", StandardScaler(), numeric_cols),
    ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_cols),
])

pipe = Pipeline([
    ("pre", pre),
    ("clf", LogisticRegression(max_iter=1000)),
])

pipe.fit(X_train, y_train)          # preprocessing is fit on TRAIN only
preds = pipe.predict(X_test)
print("F1:", f1_score(y_test, preds))
print(classification_report(y_test, preds))
```

Honest, repeated estimate via cross-validation (the whole pipeline is refit per fold):

```python
from sklearn.model_selection import cross_val_score

scores = cross_val_score(pipe, X_train, y_train, cv=5, scoring="f1")
print(f"CV F1: {scores.mean():.3f} ± {scores.std():.3f}")
```

---

## ⚠️ Pitfalls for SWEs

- **Data leakage** — the #1 killer. Fitting a scaler/encoder/imputer on the full dataset before splitting, target-encoding outside CV folds, or including a feature that secretly encodes the answer (e.g. `payment_received` when predicting `will_pay`). Symptom: implausibly high scores. Fix: do all learned preprocessing *inside* a `Pipeline`.
- **Optimizing accuracy on imbalanced data** — 99% accuracy can mean your model does literally nothing. Choose a metric that matches the cost of errors.
- **Tuning on the test set** — every time you peek at the test set to make a decision, you leak. The test set gets touched **once**, at the end. Tune on validation/CV only.
- **No baseline** — always start with a dumb model (predict the mean / the majority class — `DummyClassifier`/`DummyRegressor`). If your fancy model can't beat it, something is wrong. The baseline tells you whether ML is even helping.
- **Forgetting to set `random_state`** — non-reproducible splits make results impossible to compare. Set seeds.
- **Trusting one train/test split** — it's noisy. Use cross-validation before believing a number.

---

## 🔑 Key terms

- **Feature / label** — model input columns / the target you predict.
- **Hyperparameter** — a knob you set before training (vs. a parameter the model learns).
- **Overfitting / underfitting** — memorizing noise / being too simple to capture the pattern.
- **Bias-variance tradeoff** — the balance between being too simple and too sensitive.
- **Regularization** — penalizing complexity (L1/L2) to reduce overfitting.
- **Cross-validation** — rotating train/validation splits for a stable score.
- **Data leakage** — test/future info contaminating training; inflates scores falsely.
- **Confusion matrix** — TP/FP/TN/FN counts, the basis of classification metrics.
- **Precision / recall** — false-alarm cost / miss cost.
- **Baseline** — a trivial model your real model must beat.
- **Pipeline** — chained preprocessing + model fit as one unit (leakage-safe).
- **Ensemble** — combining many models (bagging → random forests, boosting → XGBoost).

## 📚 Best resources
- **Course** — [Andrew Ng: Machine Learning Specialization (Coursera)](https://www.coursera.org/specializations/machine-learning-introduction) — *the canonical starting point*
- **Hands-on** — [Kaggle: Intro to ML](https://www.kaggle.com/learn/intro-to-machine-learning) + [Intermediate ML](https://www.kaggle.com/learn/intermediate-machine-learning)
- **Book** — *Hands-On Machine Learning with Scikit-Learn, Keras & TensorFlow* by Aurélien Géron **(the #1 practical book — buy it)**
- **Intuition** — [StatQuest with Josh Starmer (YouTube)](https://www.youtube.com/c/joshstarmer) — *unbeatable for building intuition on every algorithm here*
- **Reference** — [scikit-learn User Guide](https://scikit-learn.org/stable/user_guide.html) — *clear, example-rich, the official source of truth*

## 🛠️ Phase project
**Win (or place on) a Kaggle competition.** Take the [Titanic](https://www.kaggle.com/c/titanic) (classification) or [House Prices](https://www.kaggle.com/c/house-prices-advanced-regression-techniques) (regression) starter comp end-to-end.

**Acceptance criteria — you're done when:**
- [ ] You did real EDA: looked at distributions, missing values, and target balance before modeling.
- [ ] You set a `DummyClassifier`/`DummyRegressor` **baseline** and recorded its score.
- [ ] All preprocessing lives inside a `Pipeline` / `ColumnTransformer` — **zero leakage**.
- [ ] You compared ≥3 algorithms including a gradient-boosting model (XGBoost or LightGBM) using **cross-validation**, not a single split.
- [ ] You tuned the best model with `GridSearchCV` or `RandomizedSearchCV` on the train set only.
- [ ] You reported the **right metric** for the task (F1/ROC-AUC for Titanic, RMSE/R² for House Prices) and beat the baseline.
- [ ] You submitted to the leaderboard and wrote a short README/blog explaining your approach, your metric choice, and how you avoided leakage.

➡️ Next: [Phase 4 — Deep Learning](04-deep-learning.md)
