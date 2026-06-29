# Phase 5 — NLP & Transformers

**Goal:** Understand how modern language models work, from tokens to attention to the transformer architecture that powers everything.
**Time:** 3–4 weeks.

---

## 🎯 Outcomes
You understand the transformer deeply enough to explain attention to a colleague, use Hugging Face confidently, and fine-tune a model that beats a classical baseline.

## ✅ Checklist

### NLP foundations
- [ ] Text preprocessing: tokenization, stemming, lemmatization
- [ ] Bag-of-words, TF-IDF
- [ ] Word embeddings: Word2Vec, GloVe (intuition) — and why static embeddings were limited
- [ ] Sequence models recap (why RNNs struggled with long context)

### The transformer (the big one)
- [ ] Tokenization in LLMs (BPE, subword) — [tiktoken](https://github.com/openai/tiktoken)
- [ ] **Self-attention & multi-head attention** (understand the intuition + the formula)
- [ ] Positional encodings
- [ ] Residual connections & layer norm in the block
- [ ] The feed-forward block & stacking layers
- [ ] Encoder vs decoder vs encoder-decoder
- [ ] Read the paper: ["Attention Is All You Need"](https://arxiv.org/abs/1706.03762)

### Model families
- [ ] BERT (encoder) — embeddings & classification
- [ ] GPT (decoder) — generation
- [ ] T5 / BART (encoder-decoder) — translation/summarization
- [ ] How pretraining + fine-tuning works

### Hugging Face ecosystem
- [ ] `transformers`: `pipeline`, `AutoModel`, `AutoTokenizer`
- [ ] `datasets` library
- [ ] The Hugging Face Hub (download/use models)
- [ ] Fine-tuning with the `Trainer` API

---

## Why this matters even for AI Engineers

You will spend most of your career *calling* models, not building them. So why learn the engine?

Because the transformer's quirks leak into everything you do at the application layer. You don't need to derive the gradients, but understanding **attention, tokenization, and context windows** is the difference between cargo-culting prompts and actually knowing why a model behaves the way it does:

- **Prompting** — knowing that a model attends to *every* token and predicts the *next* one explains why ordering, framing, and few-shot examples change outputs so dramatically.
- **RAG** — chunking, embeddings, and "lost in the middle" failures all come from how attention and context windows work. You can't tune a retrieval pipeline you don't understand.
- **Debugging weird behavior** — "why did it miscount the letters in 'strawberry'?" (tokenization). "Why did it forget the start of a long doc?" (context limits + attention dilution). "Why is my cost 4x what I expected?" (tokens != words). These stop being mysteries.

Think of this phase like learning how a database query planner works. You rarely touch it directly, but it makes you dangerous at the layer above.

---

## NLP foundations (the pre-transformer world, briefly)

Before transformers, NLP was a pipeline of hand-built steps. You should recognize these because TF-IDF baselines and classical preprocessing are still useful, and they frame *why* embeddings were such a leap.

- **Tokenization** — split text into units. Classically, words: `"cats are great"` → `["cats", "are", "great"]`.
- **Stemming** — chop words to a crude root with rules. `"running" → "run"`, `"studies" → "studi"` (not a real word — stemming is fast and dumb).
- **Lemmatization** — reduce to the real dictionary form using grammar. `"studies" → "study"`, `"better" → "good"`. Slower, smarter than stemming.
- **Bag-of-words (BoW)** — represent a document as a vector of word counts, ignoring order. `"the cat sat"` and `"sat the cat"` look identical. Simple, surprisingly strong for topic classification.
- **TF-IDF** — weight each word by *term frequency* (how often it appears here) × *inverse document frequency* (how rare it is across the corpus). Common words like "the" get crushed; distinctive words get amplified. **A TF-IDF + logistic regression model is still your honest baseline** for text classification — fast, interpretable, and shockingly hard to beat on small datasets.

### Word embeddings (Word2Vec, GloVe)
The first big leap: instead of treating words as opaque IDs, map each word to a dense vector (say 300 numbers) where **similar words land near each other**. Trained on co-occurrence ("you shall know a word by the company it keeps"), these vectors captured analogies — the famous `king − man + woman ≈ queen`.

**Why static embeddings were limited:** each word got *exactly one* vector, forever. The word "bank" has the same vector in "river bank" and "bank account." There was no way to let context shift a word's meaning. Transformers fixed exactly this: their embeddings are **contextual** — "bank" gets a different representation depending on the surrounding tokens. That single idea is most of why modern NLP works.

---

## The transformer, explained intuitively

The 2017 paper *"Attention Is All You Need"* threw out recurrence (RNNs process one token at a time, struggling to carry information across long distances) and replaced it with **attention**, which lets every token look at every other token *in parallel*. This is both why transformers capture long-range context and why they train fast on GPUs.

### Tokenization in LLMs (subword / BPE)
LLMs don't tokenize on words. They use **subword tokenization** — most commonly **Byte-Pair Encoding (BPE)** — which starts from characters and greedily merges the most frequent pairs into a fixed vocabulary (often ~30k–100k tokens).

So a token might be a whole common word, a word-piece, or even punctuation:

- `"tokenization"` → `["token", "ization"]`
- `"GPT-4"` → `["G", "PT", "-", "4"]`
- A space is usually part of the token: `" the"` differs from `"the"`.

**Key implications:**
- **token != word.** A rough rule of thumb for English is ~0.75 words per token, or ~4 characters per token. Code, JSON, and other languages tokenize *less* efficiently.
- **Cost and context are measured in tokens, not words.** A 1,000-word email is ~1,300 tokens. Your context-window budget and your API bill are both in tokens.
- **Spelling tasks confuse models** because they never see individual letters — "strawberry" might be one or two tokens, so "how many r's?" is genuinely hard for it.

Go play with the [OpenAI tokenizer / tiktoken](https://github.com/openai/tiktoken) and *watch* your sentences split. It builds intuition fast.

### Self-attention — the core idea
Here is the whole intuition in one sentence: **for each token, attention lets it look at every other token in the sequence and decide how much each one matters for understanding it right now.**

Consider: *"The animal didn't cross the street because **it** was too tired."* What does "it" refer to? You resolved that instantly using "tired" and "animal." Self-attention is the mechanism that lets the model do the same — when processing "it," it can attend strongly to "animal."

How it works mechanically — each token produces three vectors via learned weight matrices:

- **Query (Q)** — "what am I looking for?"
- **Key (K)** — "what do I offer / what am I about?"
- **Value (V)** — "the actual information I'll pass along if attended to."

For a given token, you compare its **Query** against the **Key** of every token (including itself) via dot products. High dot product = high relevance. You scale and softmax those scores into weights that sum to 1, then take a weighted sum of all the **Values**. The result is a new representation of that token that has *mixed in* information from whatever was relevant.

The whole thing is one compact formula — **scaled dot-product attention**:

```
Attention(Q, K, V) = softmax( (Q · Kᵀ) / √dₖ ) · V
```

- `Q · Kᵀ` produces the raw relevance scores between every pair of tokens.
- `/ √dₖ` (divide by the square root of the key dimension) keeps the numbers from blowing up so the softmax stays stable.
- `softmax(...)` turns scores into attention weights that sum to 1.
- `· V` takes the weighted blend of values.

Because every token can directly attend to every other token in one step, there's no "distance" to traverse — long-range dependencies are as easy to capture as short ones. That's the property RNNs lacked.

### Multi-head attention
One attention computation captures one kind of relationship. **Multi-head attention** runs several attention operations in parallel (e.g. 8 or 16 "heads"), each with its own Q/K/V projections. One head might track subject–verb agreement, another might track which noun a pronoun refers to, another positional patterns. Their outputs are concatenated and projected back down. It's like a committee of specialists looking at the sentence from different angles.

### Positional encodings
Attention by itself is **order-blind** — to it, a sentence is a bag of tokens. So we *inject* position information by adding a positional encoding to each token's embedding (the original paper used fixed sine/cosine waves; modern models often use learned or rotary positions). Now the model knows "the cat sat" differs from "sat the cat."

### Putting a block together
A transformer **block** stacks these pieces with two reliability tricks:

1. **Multi-head self-attention** (mix information across tokens), wrapped in a **residual connection** (add the input back to the output) + **layer normalization**.
2. **Feed-forward network** — a small per-token MLP (expand to ~4× width, nonlinearity, project back). This is where a lot of the model's "knowledge" lives; attention moves information around, the FFN processes it. Also wrapped in residual + layer norm.

**Residual connections** let gradients flow cleanly through dozens of layers (the same trick from ResNets in vision); **layer norm** keeps activations stable. Without these, deep transformers wouldn't train.

Then you **stack** these blocks — GPT-2 had 12–48, large models have dozens to hundreds. Each layer refines the representation a little more.

### Encoder vs decoder vs encoder-decoder
The original transformer had two halves. Modern models pick the part they need:

- **Encoder** — every token attends to *all* tokens (left and right). Builds a rich, bidirectional understanding of the *whole* input. Great for *understanding* tasks: classification, embeddings, NER. → **BERT**.
- **Decoder** — uses **causal (masked) attention**: each token can only attend to tokens *before* it, never the future. This is what lets it *generate* text one token at a time without cheating. → **GPT and essentially all modern LLMs**.
- **Encoder-decoder (seq2seq)** — encoder digests the input, decoder generates an output conditioned on it. Natural fit for translation and summarization, where input and output are different texts. → **T5, BART**.

---

## Model families

- **BERT** *(encoder)* — pretrained with **masked language modeling**: hide ~15% of tokens and predict them from both sides. The result is excellent **contextual embeddings**. Use BERT/DistilBERT/RoBERTa for classification, semantic search, and NER — not for free-form generation.
- **GPT** *(decoder)* — pretrained with **next-token prediction**: given everything so far, predict the next token. Repeat that at scale and you get generation, in-context learning, and everything that makes modern LLMs feel magical.
- **T5 / BART** *(encoder-decoder)* — frame every task as text-in → text-out ("translate English to German: ...", "summarize: ..."). Strong for summarization and translation.

### Pretraining + fine-tuning (why this is the whole game)
- **Pretraining** — train on a massive unlabeled corpus with a self-supervised objective (masked or next-token prediction). Expensive, done once, learns general language structure and world knowledge.
- **Fine-tuning** — take those pretrained weights and continue training on *your* small labeled dataset for *your* task. You inherit all that general knowledge and only teach it the specifics. This is why you can fine-tune DistilBERT on a few thousand examples and get great results — you're standing on millions of dollars of pretraining.

This "pretrain once, fine-tune cheaply" pattern (transfer learning) is the reason a small team can ship strong NLP without a supercomputer.

---

## Hugging Face ecosystem

The de facto standard toolkit. Learn these four pieces:

- **`transformers`** — the models. `pipeline` for one-line inference; `AutoModel` / `AutoTokenizer` for full control.
- **`datasets`** — efficient, memory-mapped dataset loading and processing.
- **The Hub** — hundreds of thousands of pretrained models and datasets you can pull by name.
- **`Trainer`** — a high-level training loop that handles batching, evaluation, checkpoints, and mixed precision so you don't hand-roll it.

The fastest possible inference — `pipeline` picks a sensible default model, tokenizes, runs, and decodes for you:

```python
from transformers import pipeline

clf = pipeline("sentiment-analysis")
print(clf("I genuinely loved this phase of the roadmap."))
# [{'label': 'POSITIVE', 'score': 0.9998}]
```

One level down, where you control the tokenizer and model — this is what you'll actually use for fine-tuning and embeddings:

```python
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

name = "distilbert-base-uncased-finetuned-sst-2-english"
tokenizer = AutoTokenizer.from_pretrained(name)
model = AutoModelForSequenceClassification.from_pretrained(name)

inputs = tokenizer("Attention really is all you need.", return_tensors="pt")
with torch.no_grad():
    logits = model(**inputs).logits

pred = logits.argmax(dim=-1).item()
print(model.config.id2label[pred])  # POSITIVE
```

Notice the split: `AutoTokenizer` turns text into the integer token IDs the model expects; `AutoModel...` runs the network. Every Hugging Face task follows this tokenize → model → decode shape.

---

## ⚠️ Pitfalls for SWEs

- **Confusing tokens with characters or words.** Your cost, your rate limits, and your context budget are all in *tokens*. Always measure with a tokenizer, never eyeball word counts.
- **Ignoring context-window limits.** Stuff too much in and the model silently truncates or degrades ("lost in the middle" — info buried mid-context gets under-attended). Budget your tokens deliberately.
- **Using a generative model's hidden states for search.** Embeddings from a chat/generative model are *not* the best for retrieval. Use a **dedicated embedding model** (e.g. a sentence-transformer or a purpose-built embeddings endpoint) for semantic search and RAG.
- **Assuming bigger is always better.** A fine-tuned DistilBERT can beat a giant general LLM on a narrow classification task — faster, cheaper, and more accurate. Match the model to the job.
- **Skipping the baseline.** Always build the TF-IDF + logistic regression baseline first. If your fancy fine-tune can't beat it, you've learned something important before burning GPU hours.

---

## 🔑 Key terms

- **Token** — the unit a model reads; a subword chunk, not a word.
- **BPE (Byte-Pair Encoding)** — subword tokenization that merges frequent character pairs into a fixed vocabulary.
- **Attention** — mechanism letting each token weigh the relevance of every other token.
- **Query / Key / Value** — per-token vectors: what I'm looking for / what I offer / the info I pass along. Attention = match queries to keys, blend values.
- **Multi-head attention** — several attention computations in parallel, each capturing a different kind of relationship.
- **Positional encoding** — added signal that tells the model token order (attention alone is order-blind).
- **Encoder** — bidirectional, builds understanding (BERT). **Decoder** — causal/masked, generates text (GPT). **Encoder-decoder** — input→output seq2seq (T5/BART).
- **Pretraining** — costly self-supervised training on a huge corpus to learn general language.
- **Fine-tuning** — cheaply adapting a pretrained model to your specific task with your labeled data.
- **Embedding** — a dense vector representation of text; contextual ones (from transformers) shift with surrounding tokens.

---

## 📚 Best resources
- **Visual** — [The Illustrated Transformer (Jay Alammar)](https://jalammar.github.io/illustrated-transformer/) **(read this first)**
- **Build it** — [Karpathy: Let's build GPT from scratch](https://www.youtube.com/watch?v=kCc8FmEb1nY) **(do it — type it out yourself)**
- **The paper** — [Attention Is All You Need](https://arxiv.org/abs/1706.03762) (read it *after* the Illustrated Transformer)
- **Course** — [Hugging Face NLP Course (free)](https://huggingface.co/learn/nlp-course) · [Stanford CS224N: NLP with Deep Learning](https://web.stanford.edu/class/cs224n/)
- **Reference** — [The Annotated Transformer (Harvard)](http://nlp.seas.harvard.edu/annotated-transformer/) (the paper, line by line, in PyTorch)

---

## 🛠️ Phase project
**Fine-tune a transformer and beat a baseline.** Take a pretrained DistilBERT and fine-tune it on a text-classification task (e.g. sentiment, or your own labeled data). Compare it head-to-head against a classical baseline and report the delta.

**Acceptance criteria:**
- [ ] Build a **TF-IDF + logistic regression baseline** first; record its accuracy/F1 on a held-out test set.
- [ ] Fine-tune **DistilBERT** on the *same* train/test split using `AutoTokenizer`, `AutoModelForSequenceClassification`, and the `Trainer` API.
- [ ] Report **both** models' metrics in a small table and state the delta (e.g. "DistilBERT: 0.91 F1 vs TF-IDF: 0.86 F1, +0.05").
- [ ] Write 3–4 sentences on the trade-off: the fine-tuned model's accuracy gain **vs** its added latency, size, and inference cost — and when the baseline would be the right call.
- [ ] Bonus: inspect a few examples the baseline got wrong but the transformer got right, and explain *why* context helped.

➡️ Next: [Phase 6 — LLMs & Generative AI](06-llms.md)
