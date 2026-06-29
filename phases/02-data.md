# Phase 2 — Data Wrangling & Analysis

**Goal:** Load, clean, transform, and explore data. This is ~70% of real ML work.
**Time:** 2–3 weeks.

---

## 🎯 Outcomes
You can take a messy real-world dataset and turn it into clean, analyzed, visualized insight — and you know the data-specific traps that silently break ML models.

> **Frame for SWEs:** You already know how to code. This phase isn't about syntax — it's about a different *mindset*. In app development, data is mostly trusted (you wrote the schema). In ML, data is the adversary: missing, skewed, mislabeled, leaking. The tools below (NumPy, Pandas) are how you interrogate it, and the habits matter more than the API.

## ✅ Checklist

### NumPy
- [ ] Arrays, dtypes, shapes, reshaping
- [ ] Indexing, slicing, boolean masks
- [ ] Broadcasting (key concept)
- [ ] Vectorized ops vs Python loops (and *why* they're faster)
- [ ] Axis-based reductions (`sum`, `mean`, `argmax` along an axis)

### Pandas
- [ ] `Series` & `DataFrame` mental model
- [ ] Reading CSV/JSON/Parquet/SQL
- [ ] Selecting: `loc`, `iloc`, boolean filtering
- [ ] Handling missing data (`isna`, `fillna`, `dropna`)
- [ ] `groupby`, aggregation, pivot tables
- [ ] Merging/joining DataFrames (`merge`, `concat`)
- [ ] `apply`, `map`, vectorized string ops (`.str`)
- [ ] Dates & time series basics (`to_datetime`, resampling)
- [ ] `value_counts`, `astype`, categorical dtypes

### Exploratory Data Analysis (EDA)
- [ ] Summary statistics, distributions
- [ ] Detecting outliers & data quality issues
- [ ] Correlation analysis (and why correlation ≠ causation)
- [ ] Feature understanding (categorical vs numerical vs datetime)

### Visualization
- [ ] Matplotlib (line, scatter, hist, bar)
- [ ] Seaborn (heatmaps, pairplots, distributions, box plots)
- [ ] When to use which chart

### Hygiene (don't skip — this is what separates ML from data analysis)
- [ ] Understand **data leakage** and how to spot it
- [ ] Train/test split *before* any fitting or imputation
- [ ] Reproducible notebooks (fixed random seed, runs top-to-bottom)

---

## 📦 NumPy — the array layer under everything

Every ML library (Pandas, scikit-learn, PyTorch) is NumPy arrays underneath. Learn it first.

**Arrays, dtypes, shapes.** An `ndarray` is a fixed-size, single-dtype, N-dimensional grid. Unlike a Python list, every element is the same type and stored contiguously in memory — that's what makes it fast.

```python
import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])
a.shape    # (2, 3)  -> 2 rows, 3 cols
a.dtype    # dtype('int64')
a.reshape(3, 2)        # same data, new shape
a.astype(np.float32)   # change dtype (watch memory for big arrays)
```

**Vectorization vs Python loops.** Operate on whole arrays, not element-by-element.

```python
# Slow: Python-level loop, one interpreted op per element
out = [x * 2 for x in py_list]

# Fast: one vectorized call
out = arr * 2
```

*Why it's faster:* the loop runs in the C layer with no per-element Python interpreter overhead, the data is contiguous so the CPU cache stays hot, and operations can use SIMD instructions. The speedup is often **10–100x**. Rule of thumb: if you're writing a `for` loop over array rows in ML code, you're probably doing it wrong.

**Broadcasting.** NumPy stretches smaller arrays to match shapes *without copying data*, following two rules: compare shapes right-to-left; dimensions are compatible if they're equal or one of them is 1.

```python
prices = np.array([[10], [20], [30]])   # shape (3, 1)
tax    = np.array([1.0, 1.1, 1.2])      # shape (3,) -> (1, 3)
prices * tax                            # -> (3, 3), every combo, no loop
```

A common use: subtract the per-column mean to center data — `X - X.mean(axis=0)`. The `(n, cols)` array minus the `(cols,)` mean broadcasts cleanly.

**Axis reductions.** `axis=0` collapses rows (gives per-column results); `axis=1` collapses columns (per-row). Mixing these up is the #1 NumPy bug — when in doubt, print `.shape` before and after.

---

## 🐼 Pandas — your data interrogation tool

A `Series` is a labeled 1-D array (a column). A `DataFrame` is a dict of Series sharing one index (a table). The **index** is the superpower vs a SQL table — it's a first-class, alignable label on every row.

**Loading.**

```python
import pandas as pd
df = pd.read_csv("data.csv")          # also read_parquet, read_json, read_sql
df.head(); df.info(); df.describe()   # always run these three first
```

**Selecting: `loc` vs `iloc`.** This trips up everyone. `loc` is **label-based**, `iloc` is **integer-position-based**.

```python
df.loc[10, "price"]        # row with index LABEL 10, column "price"
df.iloc[0, 2]              # row POSITION 0, column position 2
df.loc[df["price"] > 100]  # boolean filtering — the workhorse
```

**Boolean filtering** is how you slice data. Combine conditions with `&` / `|` and **wrap each in parentheses** (operator precedence will bite you otherwise):

```python
df[(df["age"] > 30) & (df["country"] == "US")]
```

**Missing data.** Real data has holes. Decide deliberately — don't just `dropna()` reflexively.

```python
df.isna().sum()                       # how many missing per column?
df["age"].fillna(df["age"].median())  # impute (median is outlier-robust)
df.dropna(subset=["target"])          # drop rows missing the LABEL
```

> ⚠️ Imputing with a statistic computed over the *whole* dataset before splitting is leakage. More below.

**`groupby`** — split / apply / combine, the SQL `GROUP BY` you already know:

```python
df.groupby("country")["revenue"].agg(["mean", "sum", "count"])
```

**Merge / join** — same semantics as SQL joins:

```python
pd.merge(orders, users, on="user_id", how="left")
pd.concat([df_jan, df_feb], axis=0)   # stack rows (axis=1 stacks columns)
```

**`apply` and vectorized strings.** Prefer vectorized methods; reach for `apply` only when there's no built-in:

```python
df["name"].str.lower().str.strip()        # vectorized, fast
df["score"].apply(lambda x: grade(x))     # row-wise Python, slower — last resort
```

**Dates.** Parse explicitly, then you get a whole `.dt` toolkit and resampling:

```python
df["ts"] = pd.to_datetime(df["ts"])
df["month"] = df["ts"].dt.month
df.set_index("ts").resample("D")["sales"].sum()   # daily totals
```

---

## 🔍 EDA workflow — a repeatable recipe

Don't model blind. Run this every time you meet a new dataset:

1. **Shape & types** — `df.shape`, `df.info()`. How many rows/cols? Any columns the wrong dtype (numbers stored as strings)?
2. **Summary stats** — `df.describe(include="all")`. Look for impossible values (negative ages, a max far above the 75th percentile = outliers).
3. **Missingness** — `df.isna().mean()`. Which columns are mostly empty? Is missingness random or systematic?
4. **Distributions** — histogram each numeric column. Skewed? Bimodal? Spike at 0 or a sentinel like -999?
5. **Categoricals** — `df["col"].value_counts()`. Rare categories, typos ("US" vs "USA"), unexpected cardinality.
6. **Outliers** — box plots or the IQR rule. Are they errors or real signal? Don't delete blindly.
7. **Correlation** — `df.corr(numeric_only=True)` + a heatmap. Spot redundant features and (carefully) relationships to the target.
8. **Data quality** — duplicates (`df.duplicated().sum()`), inconsistent units, leakage candidates (columns that "know" the answer).

The output of EDA isn't pretty charts — it's a **written list of decisions**: what to clean, drop, impute, and engineer.

---

## 📊 Visualization — which chart when

You're plotting to *think*, not to decorate. Pick by the question:

- **Distribution of one number** → histogram or KDE (`sns.histplot`). Spot skew, modes, outliers.
- **One number across categories** → bar chart (counts/means) or box/violin (spread per group).
- **Two numbers, relationship** → scatter plot (`sns.scatterplot`). Add a trend line for direction.
- **Many numeric pairs at once** → `sns.pairplot` or a correlation heatmap (`sns.heatmap`).
- **A value over time** → line chart. Time goes on the x-axis, always.
- **Counts of categories** → bar chart, sorted by value. Avoid pie charts (hard to compare angles).

Matplotlib is the low-level engine (full control, verbose); Seaborn is the friendly layer for statistical plots. Use Seaborn for EDA speed, drop to Matplotlib when you need to customize. Always label axes — a chart you can't interpret in 6 months is wasted work.

---

## 🚱 Data leakage & train/test hygiene (read this twice)

**Data leakage** is when information that won't be available at prediction time sneaks into training. The model looks brilliant in your notebook, then collapses in production. It is the single most common way ML beginners fool themselves.

**The golden rule:** *split first, then learn everything from the training set only.*

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42   # fixed seed = reproducible
)
# Fit scalers/imputers/encoders on X_train ONLY, then apply to X_test.
```

Common leaks to hunt for:

- **Preprocessing before splitting** — computing a mean, scaler, or imputation value over the full dataset leaks test info into training. Fit on train, transform test.
- **Target leakage** — a feature that's a proxy for the label or was created *after* the outcome (e.g. `was_refunded` when predicting `will_churn`). If a feature seems too predictive, suspect it.
- **Temporal leakage** — for time series, a random split lets the model "see the future." Split by time instead.
- **Duplicate / near-duplicate rows** spanning train and test inflate scores.
- **ID columns** that secretly encode the target (sorted-by-class IDs).

If your model is suspiciously accurate (99% on a hard problem), assume leakage until proven otherwise.

---

## ⚠️ Pitfalls for SWEs

Habits from app dev that backfire in data work:

- **Looping instead of vectorizing.** `for i in range(len(df)): df.loc[i, ...]` is correct, idiomatic-looking, and 100x too slow. Use vectorized ops, `groupby`, or `.str`/`.dt` accessors. `iterrows()` is almost never the answer.
- **Trusting the data because it loaded.** A clean parse is not clean data. Nulls, dupes, wrong units, and mixed types pass silently and corrupt your model. Always run `info()`, `describe()`, `isna()`, `value_counts()`.
- **Leakage.** The bug you can't see in tests because the test set was contaminated too. Treat the test set as production data you're not allowed to peek at.
- **Trusting averages.** A mean hides skew, bimodality, and outliers — Anscombe's quartet has four wildly different datasets with identical means and correlations. Always plot the distribution; report medians and quantiles for skewed data.
- **Mutating in place without copies.** Chained indexing (`df[df.x > 0]["y"] = 1`) silently fails or warns. Use `.loc` for assignment, or `.copy()` when you slice a sub-frame you'll modify.
- **Off-by-one on `axis`.** `axis=0` vs `axis=1` flips meaning; verify with `.shape`.

---

## 🔑 Key terms

- **ndarray** — NumPy's N-dimensional, single-dtype array; the base unit of numerical computing in Python.
- **Broadcasting** — automatic shape-stretching of arrays in elementwise ops, no data copied.
- **Vectorization** — replacing Python loops with whole-array operations that run in compiled C.
- **Series / DataFrame** — Pandas' labeled 1-D column and 2-D table.
- **Index** — the row labels of a Series/DataFrame; enables alignment on joins and lookups.
- **`loc` / `iloc`** — label-based vs integer-position-based selection.
- **groupby (split-apply-combine)** — partition rows, run an aggregation per group, recombine.
- **Imputation** — filling missing values with a substitute (mean/median/mode/model).
- **EDA** — Exploratory Data Analysis; the structured first look at a dataset.
- **Outlier** — a point far from the rest; may be an error or real signal — investigate, don't auto-delete.
- **Data leakage** — info from outside the training data (often the test set or future) contaminating the model.
- **Train/test split** — holding out data the model never sees during training, to estimate real-world performance.
- **Feature** — an input column/variable; **target/label** — the column you're predicting.

---

## 📚 Best resources
- **Pandas** — [Kaggle: Pandas (free micro-course)](https://www.kaggle.com/learn/pandas) · [Official 10-minute intro](https://pandas.pydata.org/docs/user_guide/10min.html)
- **NumPy** — [NumPy Quickstart](https://numpy.org/doc/stable/user/quickstart.html) · [NumPy: the absolute basics for beginners](https://numpy.org/doc/stable/user/absolute_beginners.html)
- **EDA/Viz** — [Kaggle: Data Visualization](https://www.kaggle.com/learn/data-visualization) · [Seaborn tutorial](https://seaborn.pydata.org/tutorial.html)
- **Data cleaning** — [Kaggle: Data Cleaning (free micro-course)](https://www.kaggle.com/learn/data-cleaning)
- **Book** — *Python for Data Analysis* by Wes McKinney (pandas' creator) — the definitive reference, free to read online at [wesmckinney.com/book](https://wesmckinney.com/book/)

## 🛠️ Phase project
**End-to-end EDA on a real dataset.** Pick something from [Kaggle Datasets](https://www.kaggle.com/datasets) you actually care about (ideally from your own domain). Clean it, explore it, and write up your findings in a notebook.

**Acceptance criteria:**
- [ ] Notebook runs top-to-bottom with no errors after *Restart & Run All* (reproducible).
- [ ] A data-quality section: documents missing values, duplicates, outliers, and the cleaning decisions you made (with reasoning, not just code).
- [ ] At least one `groupby` and one `merge`/join used meaningfully.
- [ ] **5 insights**, each stated in one plain-English sentence and backed by a chart or stat.
- [ ] **5 polished charts** — correct chart type for the question, labeled axes, a title each.
- [ ] No leakage in any computed feature; if you split the data, preprocessing is fit on train only.
- [ ] Markdown commentary throughout — a reader should follow your reasoning without reading the code.

➡️ Next: [Phase 3 — Classical Machine Learning](03-classical-ml.md)
