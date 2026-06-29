# Phase 6 — LLMs & Generative AI

**Goal:** Work effectively with large language models — calling them, prompting them, evaluating them, and customizing them.
**Time:** 3–4 weeks. **This is where "AI Engineer" really begins.**

---

## 🎯 Outcomes
You can build with any major LLM API, write reliable prompts, choose between prompting/RAG/fine-tuning, and evaluate output quality.

## ✅ Checklist

### Working with LLMs
- [ ] How LLMs generate text (next-token prediction, sampling)
- [ ] Tokens, context windows, and pricing
- [ ] Temperature, top-p, max tokens, stop sequences
- [ ] Calling APIs: **Anthropic Claude**, OpenAI, Google Gemini
- [ ] Structured output / JSON mode / tool calling
- [ ] Streaming responses
- [ ] Open models: Llama, Mistral, Qwen via [Ollama](https://ollama.com/) / [Hugging Face](https://huggingface.co/)

### Prompt engineering
- [ ] Zero-shot, few-shot prompting
- [ ] Chain-of-thought & reasoning prompts
- [ ] System prompts & role design
- [ ] Prompt templates & variables
- [ ] Output formatting & constraints
- [ ] Reducing hallucinations
- [ ] Prompt injection & safety basics

### Customizing models
- [ ] Prompting vs RAG vs fine-tuning — **when to use which**
- [ ] Fine-tuning basics & when it's worth it
- [ ] **PEFT / LoRA / QLoRA** (efficient fine-tuning)
- [ ] Quantization (run big models on small hardware)

### Evaluation (critical & underrated)
- [ ] Why LLM eval is hard
- [ ] Building eval sets for your task
- [ ] LLM-as-a-judge
- [ ] Metrics, regression testing prompts
- [ ] Tracking cost & latency

## 📚 Best resources
- **Build apps** — [Anthropic: Building with the Claude API docs](https://docs.anthropic.com/) · [DeepLearning.AI short courses (free)](https://www.deeplearning.ai/short-courses/)
- **Prompting** — [Anthropic Prompt Engineering guide](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview) · [OpenAI Cookbook](https://cookbook.openai.com/)
- **Concepts** — [Karpathy: Intro to LLMs (1hr talk)](https://www.youtube.com/watch?v=zjkBMFhNj_g) · [Hugging Face LLM Course](https://huggingface.co/learn)
- **Fine-tuning** — [Hugging Face PEFT docs](https://huggingface.co/docs/peft) · [Unsloth (fast LoRA)](https://github.com/unslothai/unsloth)

## 🛠️ Phase project
**Build an LLM-powered app** with a real use case (not a chatbot clone): e.g. a document summarizer, a code reviewer, a structured-data extractor. Must include: system prompt design, structured output, error handling, and a small eval set proving it works. Deploy it.

➡️ Next: [Phase 7 — AI Engineering: RAG & Vector DBs](07-ai-engineering-rag.md)
