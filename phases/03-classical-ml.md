# Phase 3 — Classical Machine Learning

**Goal:** Master the core ML algorithms and the workflow of training/evaluating models with scikit-learn.
**Time:** 4–5 weeks. **This is the heart of being an ML engineer.**

---

## 🎯 Outcomes
You can frame a problem as supervised/unsupervised, pick an algorithm, train it, evaluate it honestly, and avoid overfitting.

## ✅ Checklist

### Core concepts
- [ ] Supervised vs unsupervised vs reinforcement learning
- [ ] Features, labels, training/validation/test split
- [ ] Overfitting vs underfitting, bias-variance tradeoff
- [ ] Cross-validation (k-fold)
- [ ] Feature scaling (standardization, normalization)
- [ ] Feature engineering & encoding (one-hot, label, target)
- [ ] Regularization (L1/Lasso, L2/Ridge)
- [ ] The full ML pipeline (`sklearn.Pipeline`)

### Supervised — regression
- [ ] Linear regression
- [ ] Polynomial regression

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

## 📚 Best resources
- **Course** — [Andrew Ng: Machine Learning Specialization (Coursera)](https://www.coursera.org/specializations/machine-learning-introduction) — *the canonical starting point*
- **Hands-on** — [Kaggle: Intro to ML](https://www.kaggle.com/learn/intro-to-machine-learning) + [Intermediate ML](https://www.kaggle.com/learn/intermediate-machine-learning)
- **Book** — *Hands-On Machine Learning with Scikit-Learn, Keras & TensorFlow* by Aurélien Géron **(the #1 practical book — buy it)**
- **Intuition** — [StatQuest ML playlist](https://www.youtube.com/playlist?list=PLblh5JKOoLUICTaGLRoHQDuF_7q2GfuJF)

## 🛠️ Phase project
**Win (or place on) a Kaggle competition.** Do the [Titanic](https://www.kaggle.com/c/titanic) or [House Prices](https://www.kaggle.com/c/house-prices-advanced-regression-techniques) starter comp end-to-end: EDA → feature engineering → model selection → tuning → submission. Then write a blog post / README explaining your approach.

➡️ Next: [Phase 4 — Deep Learning](04-deep-learning.md)
