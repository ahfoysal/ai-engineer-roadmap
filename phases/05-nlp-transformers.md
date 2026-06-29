# Phase 5 — NLP & Transformers

**Goal:** Understand how modern language models work, from tokens to attention to the transformer architecture that powers everything.
**Time:** 3–4 weeks.

---

## 🎯 Outcomes
You understand the transformer deeply enough to explain attention, use Hugging Face confidently, and fine-tune a model.

## ✅ Checklist

### NLP foundations
- [ ] Text preprocessing: tokenization, stemming, lemmatization
- [ ] Bag-of-words, TF-IDF
- [ ] Word embeddings: Word2Vec, GloVe (intuition)
- [ ] Sequence models recap (why RNNs struggled with long context)

### The transformer (the big one)
- [ ] Tokenization in LLMs (BPE, subword) — [tiktoken](https://github.com/openai/tiktoken)
- [ ] **Self-attention & multi-head attention** (understand the math)
- [ ] Positional encodings
- [ ] Encoder vs decoder vs encoder-decoder
- [ ] Residual connections & layer norm in the block
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

## 📚 Best resources
- **Visual** — [The Illustrated Transformer (Jay Alammar)](https://jalammar.github.io/illustrated-transformer/) **(read this first)**
- **Build it** — [Karpathy: Let's build GPT from scratch](https://www.youtube.com/watch?v=kCc8FmEb1nY) **(do it)**
- **Course** — [Hugging Face NLP Course (free)](https://huggingface.co/learn/nlp-course) · [Stanford CS224N: NLP with Deep Learning](https://web.stanford.edu/class/cs224n/)
- **Reference** — [The Annotated Transformer (Harvard)](http://nlp.seas.harvard.edu/annotated-transformer/)

## 🛠️ Phase project
**Fine-tune a transformer.** Take a pretrained BERT/DistilBERT and fine-tune it on a text-classification task (e.g. sentiment, your own labeled data). Compare against a TF-IDF + logistic regression baseline and report the difference.

➡️ Next: [Phase 6 — LLMs & Generative AI](06-llms.md)
