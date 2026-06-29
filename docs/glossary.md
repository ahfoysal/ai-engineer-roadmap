# 📖 Glossary & Cheat Sheet

Every key term from across the roadmap, in one place. Alphabetical. The `→` tag points to the module where it's taught in depth.

> Use this as a quick-reference while you build, or as last-minute interview review. For the deep explanation, follow the module link.

---

## A
- **Agent** — an LLM running in a loop that chooses and runs tools to reach a goal. → [M8](../phases/08-agents.md)
- **AMP (Automatic Mixed Precision)** — training in fp16/bf16 for speed and memory, with an fp32 master copy for stability. → [M4](../phases/04-deep-learning.md)
- **ANN (Approximate Nearest Neighbor)** — fast, slightly-lossy similarity search over vectors. → [M7](../phases/07-ai-engineering-rag.md)
- **Attention** — mechanism letting each token weigh the relevance of every other token. → [M5](../phases/05-nlp-transformers.md)
- **Autoregressive generation** — producing text one sampled token at a time, feeding each back in. → [M6](../phases/06-llms.md)

## B
- **Backpropagation** — the chain rule applied through a network to compute gradients. → [M1](../phases/01-math-stats.md) / [M4](../phases/04-deep-learning.md)
- **Baseline** — a trivial model your real model must beat (e.g. TF-IDF + logistic regression). → [M3](../phases/03-classical-ml.md)
- **Batch / Epoch / Iteration** — subset processed per step / one full pass over the data / one batch step. → [M4](../phases/04-deep-learning.md)
- **Bayes' theorem** — rule for updating a belief given new evidence. → [M1](../phases/01-math-stats.md)
- **Bias-variance tradeoff** — the balance between a model being too simple (bias) and too sensitive (variance). → [M3](../phases/03-classical-ml.md)
- **BM25** — classic keyword-ranking algorithm (TF-IDF family); the keyword half of hybrid search. → [M7](../phases/07-ai-engineering-rag.md)
- **BPE (Byte-Pair Encoding)** — subword tokenization that merges frequent character pairs into a fixed vocabulary. → [M5](../phases/05-nlp-transformers.md)
- **Broadcasting** — automatic shape-stretching of arrays in elementwise ops, no data copied. → [M2](../phases/02-data.md)

## C
- **Chunking** — splitting documents into retrieval-sized pieces; the highest-leverage RAG decision. → [M7](../phases/07-ai-engineering-rag.md)
- **Confusion matrix** — TP/FP/TN/FN counts; the basis of classification metrics. → [M3](../phases/03-classical-ml.md)
- **Context window** — max tokens (input + output) a model can handle in one call. → [M6](../phases/06-llms.md)
- **Cosine similarity** — dot product of unit vectors; similarity by angle (−1 to 1). Powers embedding search. → [M1](../phases/01-math-stats.md) / [M7](../phases/07-ai-engineering-rag.md)
- **Cross-validation** — rotating train/validation splits (k-fold) for a stable performance estimate. → [M3](../phases/03-classical-ml.md)

## D
- **Data leakage** — info from outside the training data (test set / future) contaminating the model; inflates scores falsely. → [M2](../phases/02-data.md) / [M3](../phases/03-classical-ml.md)
- **Distribution** — how probability is spread over possible values (normal, Bernoulli, binomial). → [M1](../phases/01-math-stats.md)
- **Dot product** — element-wise multiply then sum; measures alignment of two vectors. → [M1](../phases/01-math-stats.md)
- **Drift** — gradual change in input distribution or output quality that silently degrades a system. → [M9](../phases/09-mlops-production.md)
- **DataFrame / Series** — Pandas' labeled 2-D table / 1-D column. → [M2](../phases/02-data.md)

## E
- **EDA (Exploratory Data Analysis)** — the structured first look at a dataset. → [M2](../phases/02-data.md)
- **Embedding** — a dense vector encoding the meaning of text; contextual ones shift with surrounding tokens. → [M5](../phases/05-nlp-transformers.md) / [M7](../phases/07-ai-engineering-rag.md)
- **Ensemble** — combining many models (bagging → random forests, boosting → XGBoost). → [M3](../phases/03-classical-ml.md)
- **Eval gate** — a CI check that runs an eval set and blocks deploy if quality regresses; the LLM analogue of "tests must pass." → [M9](../phases/09-mlops-production.md)
- **Eval set** — a fixed set of inputs + criteria to measure and regression-test model/prompt behavior. → [M6](../phases/06-llms.md)
- **Expectation** — long-run probability-weighted average. → [M1](../phases/01-math-stats.md)
- **Experiment tracking** — recording each run's params, metrics, and artifacts (W&B/MLflow) for reproducibility. → [M9](../phases/09-mlops-production.md)

## F
- **Fallback (model failover)** — routing to a secondary model/provider when the primary errors, times out, or rate-limits. → [M9](../phases/09-mlops-production.md)
- **Feature / Label (target)** — an input column / the column you're predicting. → [M2](../phases/02-data.md) / [M3](../phases/03-classical-ml.md)
- **Feature engineering** — turning raw data into features a model can use; often the biggest win. → [M3](../phases/03-classical-ml.md)
- **Fine-tuning** — updating a pretrained model's weights on your examples to change behavior. → [M5](../phases/05-nlp-transformers.md) / [M6](../phases/06-llms.md)

## G
- **Gradient (∇)** — vector of partial derivatives; points uphill, so we step the opposite way. → [M1](../phases/01-math-stats.md)
- **Gradient descent** — iteratively stepping weights downhill along the negative gradient to minimize loss. → [M1](../phases/01-math-stats.md)
- **Grounding** — answering strictly from retrieved evidence, with citations. → [M7](../phases/07-ai-engineering-rag.md)
- **Guardrail** — a check/constraint (limits, validators, approvals) keeping an agent within safe bounds. → [M8](../phases/08-agents.md)
- **groupby (split-apply-combine)** — partition rows, aggregate per group, recombine. → [M2](../phases/02-data.md)

## H
- **Hallucination** — confident, fluent, made-up model output. → [M6](../phases/06-llms.md)
- **HNSW** — graph-based ANN index; the common default for fast vector search. → [M7](../phases/07-ai-engineering-rag.md)
- **Human-in-the-loop** — a human approval step before risky or irreversible actions. → [M8](../phases/08-agents.md)
- **Hybrid search** — combining keyword (BM25) and dense vector search. → [M7](../phases/07-ai-engineering-rag.md)
- **Hyperparameter** — a setting you choose before training (lr, layers, k) vs. a parameter the model learns. → [M3](../phases/03-classical-ml.md) / [M4](../phases/04-deep-learning.md)

## I–L
- **Imputation** — filling missing values with a substitute (mean/median/mode/model). → [M2](../phases/02-data.md)
- **Index (Pandas)** — the row labels of a Series/DataFrame; enables alignment on joins/lookups. → [M2](../phases/02-data.md)
- **`loc` / `iloc`** — label-based vs integer-position-based selection in Pandas. → [M2](../phases/02-data.md)
- **Latent vector** — a compressed internal representation (e.g. an autoencoder's bottleneck). → [M4](../phases/04-deep-learning.md)
- **Learning rate (α)** — step size in gradient descent; the single most important DL knob. → [M1](../phases/01-math-stats.md) / [M4](../phases/04-deep-learning.md)
- **LLM-as-judge** — using an LLM to score other LLM outputs against a rubric. → [M6](../phases/06-llms.md)
- **LLMOps** — ops specific to LLM apps: prompt/response logging, tracing, quality+cost+latency monitoring, evals, guardrails. → [M9](../phases/09-mlops-production.md)
- **Logits** — raw, unnormalized model outputs before softmax/sigmoid. → [M4](../phases/04-deep-learning.md)
- **LoRA / QLoRA / PEFT** — efficient fine-tuning of a small set of adapter parameters. → [M6](../phases/06-llms.md)
- **Loss / cost function** — the number we minimize (how wrong the model is). → [M1](../phases/01-math-stats.md)

## M
- **Max tokens** — hard cap on generated output length. → [M6](../phases/06-llms.md)
- **MCP (Model Context Protocol)** — open standard for connecting models to tools and data sources. → [M8](../phases/08-agents.md)
- **MLE (Maximum Likelihood Estimation)** — choosing parameters that make the observed data most probable. → [M1](../phases/01-math-stats.md)
- **Model registry** — versioned catalogue of models with stages (staging/prod) and lineage that deploys promote from. → [M9](../phases/09-mlops-production.md)
- **Multi-head attention** — several attention computations in parallel, each capturing a different relationship. → [M5](../phases/05-nlp-transformers.md)

## N–O
- **ndarray** — NumPy's N-dimensional, single-dtype array; the base unit of numerical Python. → [M2](../phases/02-data.md)
- **Norm (L1/L2)** — the "length" of a vector (L1 = sum of abs, L2 = straight-line). Used in loss & regularization. → [M1](../phases/01-math-stats.md)
- **Orchestrator** — a lead agent that decomposes a task and delegates to worker agents. → [M8](../phases/08-agents.md)
- **Outlier** — a point far from the rest; may be error or real signal — investigate, don't auto-delete. → [M2](../phases/02-data.md)
- **Overfitting / Underfitting** — memorizing noise (great train, bad test) / too simple to fit the pattern at all. → [M3](../phases/03-classical-ml.md) / [M4](../phases/04-deep-learning.md)

## P
- **Parameter** — a learnable weight or bias inside the model. → [M4](../phases/04-deep-learning.md)
- **PCA** — finding directions of greatest variance to reduce dimensions. → [M1](../phases/01-math-stats.md)
- **Pipeline (sklearn)** — chained preprocessing + model fit as one leakage-safe unit. → [M3](../phases/03-classical-ml.md)
- **Positional encoding** — added signal telling the model token order (attention alone is order-blind). → [M5](../phases/05-nlp-transformers.md)
- **Precision / Recall** — false-alarm cost / miss cost; combine into F1. → [M3](../phases/03-classical-ml.md)
- **Pretraining** — costly self-supervised training on a huge corpus to learn general language. → [M5](../phases/05-nlp-transformers.md)
- **Prompt (system / user / assistant)** — standing instructions / the human's input / the model's prior replies. → [M6](../phases/06-llms.md)

## Q–R
- **Quantization** — lower-precision weights for smaller, faster models. → [M6](../phases/06-llms.md)
- **Query / Key / Value** — per-token attention vectors: what I seek / what I offer / the info I pass along. → [M5](../phases/05-nlp-transformers.md)
- **RAG (Retrieval-Augmented Generation)** — putting retrieved knowledge into the prompt for grounded answers. → [M6](../phases/06-llms.md) / [M7](../phases/07-ai-engineering-rag.md)
- **ReAct** — agent pattern interleaving reasoning and acting (tool calls) step by step. → [M8](../phases/08-agents.md)
- **Regularization** — penalizing complexity (L1/L2, dropout, weight decay) to reduce overfitting. → [M3](../phases/03-classical-ml.md) / [M4](../phases/04-deep-learning.md)
- **Reranking** — re-scoring a candidate shortlist with a heavier cross-encoder for better precision. → [M7](../phases/07-ai-engineering-rag.md)

## S–T
- **Semantic cache** — caches responses by meaning (embedding similarity), so paraphrased queries hit the cache. → [M9](../phases/09-mlops-production.md)
- **Stop sequence** — a string that halts generation when produced. → [M6](../phases/06-llms.md)
- **Structured output** — schema-constrained, machine-readable output (e.g. JSON via tool calling). → [M6](../phases/06-llms.md)
- **Temperature / top-p / top-k** — knobs controlling randomness when sampling the next token. → [M6](../phases/06-llms.md)
- **Token** — the unit a model reads/writes (~¾ word); you pay per token. → [M5](../phases/05-nlp-transformers.md) / [M6](../phases/06-llms.md)
- **Token cost** — per-request price driven by input + output token counts. → [M9](../phases/09-mlops-production.md)
- **Tool / function calling** — the model emitting a structured request your code executes. → [M6](../phases/06-llms.md) / [M8](../phases/08-agents.md)
- **Trajectory** — the full sequence of decisions and tool calls an agent took in a run. → [M8](../phases/08-agents.md)
- **Train/test split** — holding out data the model never sees, to estimate real-world performance. → [M2](../phases/02-data.md) / [M3](../phases/03-classical-ml.md)
- **Transformer** — the attention-based architecture under every modern LLM. → [M5](../phases/05-nlp-transformers.md)

## U–Z
- **Vectorization** — replacing Python loops with whole-array operations that run in compiled C (10–100× faster). → [M2](../phases/02-data.md)
- **Vector DB** — store optimized for nearest-neighbor search over embeddings (Chroma, Qdrant, pgvector, Pinecone). → [M7](../phases/07-ai-engineering-rag.md)
- **Workflow (vs agent)** — LLM steps wired together by code you control, vs an agent that picks its own path. → [M8](../phases/08-agents.md)

---

⬅️ Back to [README](../README.md) · Modules: [0](../phases/00-foundations.md) · [1](../phases/01-math-stats.md) · [2](../phases/02-data.md) · [3](../phases/03-classical-ml.md) · [4](../phases/04-deep-learning.md) · [5](../phases/05-nlp-transformers.md) · [6](../phases/06-llms.md) · [7](../phases/07-ai-engineering-rag.md) · [8](../phases/08-agents.md) · [9](../phases/09-mlops-production.md) · [10](../phases/10-career.md)
