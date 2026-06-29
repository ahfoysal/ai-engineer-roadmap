# Phase 6 — LLMs & Generative AI

**Goal:** Work effectively with large language models — calling them, prompting them, evaluating them, and customizing them.
**Time:** 3–4 weeks. **This is where "AI Engineer" really begins.**

---

## 🎯 Outcomes
You can build with any major LLM API, write reliable prompts, choose between prompting/RAG/fine-tuning, and evaluate output quality. You treat an LLM as a component you can reason about, test, and budget for — not magic.

## ✅ Checklist

### Working with LLMs
- [ ] How LLMs generate text (next-token prediction, sampling)
- [ ] Tokens, tokenization, and how text maps to token IDs
- [ ] Context windows and why they bound everything
- [ ] Pricing: input vs output tokens, why output is more expensive
- [ ] Temperature, top-p, top-k, max tokens, stop sequences
- [ ] System vs user vs assistant roles
- [ ] Calling APIs: **Anthropic Claude**, OpenAI, Google Gemini
- [ ] Structured output / JSON mode / schema-constrained output
- [ ] Tool / function calling — definitions, the call loop, results
- [ ] Streaming responses
- [ ] Multi-turn conversations (the API is stateless — you resend history)
- [ ] Open models: Llama, Mistral, Qwen via [Ollama](https://ollama.com/) / [Hugging Face](https://huggingface.co/)

### Prompt engineering
- [ ] Zero-shot and few-shot prompting
- [ ] Chain-of-thought & reasoning prompts
- [ ] System prompt design (role, constraints, output format)
- [ ] Prompt templates & variables
- [ ] Output formatting & constraints
- [ ] Reducing hallucinations (grounding, "say I don't know")
- [ ] Prompt injection & safety basics

### Customizing models
- [ ] Prompting vs RAG vs fine-tuning — **when to use which**
- [ ] Fine-tuning basics & when it's worth it (rarely — try prompting/RAG first)
- [ ] **PEFT / LoRA / QLoRA** (efficient fine-tuning)
- [ ] Quantization (run big models on small hardware)

### Evaluation (critical & underrated)
- [ ] Why LLM eval is hard
- [ ] Building eval sets for your task
- [ ] LLM-as-a-judge
- [ ] Metrics, regression-testing prompts
- [ ] Tracking cost & latency

---

## 🧠 Mental model for SWEs

Strip away the hype and an LLM is a **stateless pure function**:

```
(prompt) -> probability distribution over the next token
```

That's the whole thing. Given some text, the model outputs a probability for *every* token in its vocabulary being the next one. To generate a full response, you:

1. Feed the prompt in, get the distribution, **sample** one token from it.
2. Append that token to the prompt.
3. Repeat — feed the longer prompt back in, sample the next token.
4. Stop when you hit a stop token, a stop sequence, or the max-token limit.

This loop is called **autoregressive generation**. Three consequences fall straight out of it, and they explain most of what feels strange about LLMs:

- **It's non-deterministic.** You're *sampling* from a distribution, so the same prompt can give different outputs. (Even at "temperature 0" you get only *near*-determinism — floating-point and batching effects mean identical strings aren't guaranteed.)
- **There's no memory between calls.** The model is a pure function. Any "conversation" you see is the client resending the entire history on every call. Lose the history, lose the memory.
- **Cost and latency scale with tokens.** Every generated token requires another forward pass. Long outputs are slow and expensive; long inputs cost too, but are processed in parallel so they're cheaper per token.

### Tokens
Models don't see characters or words — they see **tokens**, chunks of text (roughly ¾ of a word in English, fewer for code or non-English). `"hello"` might be one token; `"antidisestablishmentarianism"` several. You pay per token and your context window is measured in tokens, so "how many tokens is this?" is a question you'll ask constantly. **Don't estimate with a word count or an OpenAI tokenizer like `tiktoken` for Claude** — they disagree by 15–20%+. Use the provider's token-counting endpoint.

### Context window
The maximum number of tokens (input + output) the model can attend to in one call. Modern models range from ~200K to 1M tokens. Everything — system prompt, conversation history, retrieved documents, the user's question, and the room to answer — must fit. Run out of room and you must truncate, summarize, or retrieve more selectively (that's what Phase 7's RAG is for).

---

## ⚙️ How it works

### Tokenization
Text → token IDs (integers) via a learned tokenizer (BPE-style). The model operates entirely on IDs and converts back to text on the way out. Practical upshots: token counts aren't intuitive, whitespace and casing matter, and the same content can tokenize differently across model families.

### Sampling: temperature, top-p, top-k
These control *how* you pick from the next-token distribution:
- **Temperature** (typically 0–1): flattens or sharpens the distribution. Low (0–0.3) → focused, repeatable, good for extraction/classification/code. High (0.7–1.0) → varied, creative.
- **Top-p (nucleus)**: sample only from the smallest set of tokens whose probabilities sum to *p* (e.g. 0.9). Caps the long tail of unlikely tokens.
- **Top-k**: sample only from the *k* most likely tokens.

Rule of thumb: set **one** of temperature or top-p, not both. For most application work, low temperature. (Note: some newer reasoning models remove these knobs entirely and steer behavior through prompting and "effort" settings instead — check your provider's docs.)

### Max tokens
A hard ceiling on the *output* length. Hit it and the response is truncated mid-sentence with a `max_tokens` stop reason — your code must detect and handle this. Set it high enough to finish, low enough to bound cost. For long outputs, stream (below) so you don't hit request timeouts.

### Stop sequences
Strings that, when generated, halt output immediately (and aren't included in the result). Useful for fenced formats — e.g. stop at `</answer>` or a closing delimiter.

### Roles: system, user, assistant
Chat APIs structure input as a list of messages with roles:
- **system** — the standing instructions: who the model is, constraints, output format, tone. Set once, applies to the whole conversation.
- **user** — what the human said.
- **assistant** — what the model said (you include prior assistant turns to give it conversational memory).

### Streaming
Instead of waiting for the full response, you receive tokens as they're generated (Server-Sent Events under the hood). Better perceived latency in UIs, and it avoids HTTP timeouts on long generations. The SDK gives you both a token-by-token stream and a helper to assemble the final message.

### Structured output / JSON mode
When you need machine-readable output, don't just *ask* for JSON and hope — **constrain** it. Modern APIs let you pass a JSON schema and guarantee the response validates against it (often surfaced as a `messages.parse()` helper that returns a typed object). This replaces the old, brittle "prefill `{` and pray" trick.

### Tool / function calling
This is how LLMs *do* things beyond emitting text. You describe tools (name, description, JSON-schema inputs); the model decides when to call one and emits a structured **tool-use request** instead of a final answer. The mechanics:

1. You send the user message **plus tool definitions**.
2. The model responds with either a normal answer **or** a `tool_use` block (`stop_reason: "tool_use"`).
3. **You** execute the tool in your code and send the result back as a `tool_result`.
4. The model continues, now able to use that result — possibly calling more tools, until it produces a final answer.

The model never runs your code; it just asks. You own the loop, the security, and the side effects. Most SDKs offer a "tool runner" helper that drives this loop for you.

---

## 💻 Code: the Anthropic Claude API

Install: `pip install anthropic`. Set `ANTHROPIC_API_KEY` in your environment — never hardcode keys.

### Basic call

```python
import anthropic

client = anthropic.Anthropic()

response = client.messages.create(
    model="claude-opus-4-8",
    max_tokens=1024,
    system="You are a concise assistant. Answer in one sentence.",
    messages=[
        {"role": "user", "content": "What is a context window?"}
    ],
)

# content is a list of typed blocks — check .type before reading .text
for block in response.content:
    if block.type == "text":
        print(block.text)
```

### Structured output (schema-constrained, with Pydantic)

```python
from pydantic import BaseModel
import anthropic

class Ticket(BaseModel):
    summary: str
    priority: str          # "low" | "medium" | "high"
    needs_human: bool

client = anthropic.Anthropic()

response = client.messages.parse(
    model="claude-opus-4-8",
    max_tokens=512,
    messages=[{
        "role": "user",
        "content": "Customer: 'My prod database is down and I'm losing money NOW.'",
    }],
    output_format=Ticket,
)

ticket = response.parsed_output       # a validated Ticket instance
print(ticket.priority, ticket.needs_human)
```

### Streaming

```python
import anthropic

client = anthropic.Anthropic()

with client.messages.stream(
    model="claude-opus-4-8",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Write a haiku about databases."}],
) as stream:
    for text in stream.text_stream:
        print(text, end="", flush=True)

    final = stream.get_final_message()   # full message after streaming
    print("\ntokens:", final.usage.output_tokens)
```

### Tool calling (one round trip)

```python
import anthropic

client = anthropic.Anthropic()

tools = [{
    "name": "get_weather",
    "description": "Get the current weather for a city.",
    "input_schema": {
        "type": "object",
        "properties": {"city": {"type": "string", "description": "City name"}},
        "required": ["city"],
    },
}]

messages = [{"role": "user", "content": "What's the weather in Paris?"}]

response = client.messages.create(
    model="claude-opus-4-8", max_tokens=1024, tools=tools, messages=messages,
)

# The model asked to call a tool. Execute it, then send the result back.
if response.stop_reason == "tool_use":
    tool_use = next(b for b in response.content if b.type == "tool_use")
    result = f"18C and sunny in {tool_use.input['city']}"   # your real implementation

    messages.append({"role": "assistant", "content": response.content})
    messages.append({"role": "user", "content": [{
        "type": "tool_result",
        "tool_use_id": tool_use.id,
        "content": result,
    }]})

    final = client.messages.create(
        model="claude-opus-4-8", max_tokens=1024, tools=tools, messages=messages,
    )
    print(next(b.text for b in final.content if b.type == "text"))
```

> The other providers (OpenAI, Gemini) follow the same shapes — messages with roles, a tool-call loop, streaming, structured output. Learn one deeply and the rest transfer.

---

## ✍️ Prompting techniques

Prompting is the highest-leverage skill in this phase. You'll get more from a better prompt than from a bigger model far more often than you'd expect.

- **Zero-shot** — just ask. `"Classify the sentiment as positive, negative, or neutral: <text>"`. Works for tasks the model already understands.
- **Few-shot** — show 2–5 examples of input→output before the real input. Pins down format and edge cases:
  ```
  Review: "Loved it!" -> positive
  Review: "Total waste of money." -> negative
  Review: "It arrived on time." -> neutral
  Review: "<new review>" ->
  ```
- **Chain-of-thought (CoT)** — ask the model to reason step by step before answering. Improves accuracy on math, logic, and multi-step tasks: `"Think step by step, then give the final answer on a new line prefixed with 'Answer:'."` (Newer "reasoning" models do this internally — don't double up.)
- **System prompt design** — put the durable stuff here: role (`"You are a senior tax accountant"`), hard constraints (`"Only use information from the provided document"`), output format, and what to do when uncertain. Be specific and positive ("do X") rather than piling on "don't" rules.
- **Reducing hallucinations** — ground the model in provided context and tell it the escape hatch: *"Answer only from the context below. If the answer isn't there, say 'I don't know.'"* Ask for citations/quotes. Lower temperature. The model will confidently invent facts otherwise — this is the #1 thing that bites SWEs.

---

## 🧭 Prompting vs RAG vs fine-tuning — when to use which

Reach for these in order. Most problems are solved by the first two.

- **Prompting** — first resort, always. Zero infra, instant iteration. Use when the model already knows the domain and you just need to shape behavior or format. If a better prompt fixes it, you're done.
- **RAG (Retrieval-Augmented Generation)** — when the model needs **knowledge it doesn't have**: your docs, your data, anything past its training cutoff, or anything that changes. You retrieve relevant text and put it *in the prompt* at query time. This is Phase 7 — it's the workhorse of real LLM apps. Use it for "answer questions about *our* stuff" and to cut hallucinations.
- **Fine-tuning** — when you need to change the model's **behavior or style** in a way prompting can't, you have hundreds-plus high-quality examples, and you've already exhausted prompting + RAG. Good for: a very specific output format/tone, a narrow classification task at scale, or shrinking a prompt that's too long/expensive. It does **not** teach the model new facts reliably — use RAG for facts.

Decision shortcut: *Behavior problem → prompt, then fine-tune. Knowledge problem → RAG.*

---

## 🔧 Fine-tuning (when you actually need it)

You'll rarely do this early on, but know the landscape:

- **Full fine-tuning** updates all the model's weights — expensive, needs lots of data and GPUs. Almost never the right first move.
- **PEFT (Parameter-Efficient Fine-Tuning)** updates a tiny fraction of parameters. Far cheaper, runs on modest hardware.
  - **LoRA** — inserts small trainable "adapter" matrices alongside the frozen base weights. You train and ship just the adapters (megabytes, not gigabytes).
  - **QLoRA** — LoRA on top of a **quantized** base model, so you can fine-tune large models on a single consumer GPU.
- **Quantization** — storing weights at lower precision (e.g. 4-bit instead of 16-bit). Shrinks memory and speeds inference with modest quality loss. It's how you run a big open model on a laptop or one GPU — independent of fine-tuning, also used for plain inference.

Tooling to know: Hugging Face [`peft`](https://huggingface.co/docs/peft), `transformers`, `bitsandbytes` (quantization), and [Unsloth](https://github.com/unslothai/unsloth) for fast LoRA. For hosted models, providers offer managed fine-tuning APIs — check whether that's cheaper than self-hosting before you spin up GPUs.

---

## 📊 Evaluation (the part everyone skips)

If you take one thing from this phase: **you cannot ship an LLM feature you can't evaluate.** Because output is non-deterministic and open-ended, "it worked when I tried it" is not evidence. Eval is what separates a demo from a product.

**Why it's hard:** there's usually no single correct answer, outputs are free text, and small prompt changes cause silent regressions you won't notice without measurement.

**Build an eval set.** Collect 20–200 representative inputs with either expected outputs or pass/fail criteria. Pull real examples (including the ones that broke), not just happy paths. This is your regression suite — run it on every prompt or model change.

**Pick the right grader per task:**
- **Exact/structural checks** — for classification, extraction, JSON: assert on parsed fields, valid schema, label matches. Cheap and deterministic; use wherever the output is structured.
- **LLM-as-judge** — for open-ended quality (helpfulness, faithfulness, tone): have a (often stronger) model score outputs against a rubric. Powerful but imperfect — validate the judge against human ratings on a sample, and beware its biases (length, position, self-preference).
- **Human review** — the ground truth for the subjective stuff; sample it to calibrate everything else.

**Regression-test prompts like code.** When you tweak a prompt, rerun the eval set and compare scores before/after. A change that fixes one case often breaks three others — only measurement catches it.

**Track cost & latency as first-class metrics.** Log input/output tokens, dollars, and wall-clock per request. A "better" prompt that doubles tokens or latency may be a net loss. Watch for cost blowups from long contexts, retries, and runaway agent loops.

---

## ⚠️ Pitfalls for SWEs

- **It's non-deterministic — don't unit-test exact strings.** Assert on structure, properties, or a rubric (eval), not `assert output == "..."`. That test will flake.
- **Don't over-trust the output.** Models hallucinate fluently and confidently. Verify anything load-bearing; never put raw model output straight into a query, a shell, or a financial action.
- **Prompt injection is real.** Untrusted text (user input, retrieved docs, web pages) can contain instructions that hijack your prompt ("ignore previous instructions and..."). Don't blindly concatenate untrusted content into a privileged prompt; separate instructions from data, and constrain what tools can do.
- **Cost blowups sneak up on you.** Long context resent every turn, big `max_tokens`, retries, and agent loops multiply spend fast. Set max-token ceilings, cap loop iterations, and watch your token dashboards.
- **Context-window limits bound everything.** History grows every turn; eventually you must truncate, summarize, or retrieve selectively. Plan for it from the start.
- **The API is stateless.** "It forgot what I said" almost always means you didn't resend the history.

---

## 🔑 Key terms

- **Token** — the unit of text the model reads/writes (~¾ word). You pay per token.
- **Tokenization** — converting text to token IDs and back.
- **Context window** — max tokens (input + output) per call.
- **Autoregressive generation** — producing text one sampled token at a time, in a loop.
- **Temperature / top-p / top-k** — knobs controlling randomness when sampling the next token.
- **Max tokens** — hard cap on output length.
- **Stop sequence** — string that halts generation.
- **System prompt** — standing instructions for the whole conversation.
- **Hallucination** — confident, fluent, made-up output.
- **Tool / function calling** — the model requesting a structured action your code executes.
- **Structured output** — schema-constrained, machine-readable output (e.g. JSON).
- **RAG** — Retrieval-Augmented Generation: putting retrieved knowledge into the prompt.
- **Fine-tuning** — updating model weights on your examples to change behavior.
- **LoRA / QLoRA / PEFT** — efficient fine-tuning of a small set of adapter parameters.
- **Quantization** — lower-precision weights for smaller, faster models.
- **LLM-as-judge** — using an LLM to score other LLM outputs against a rubric.
- **Eval set** — a fixed set of inputs + criteria used to measure and regression-test.

---

## 📚 Best resources
- **Build apps** — [Anthropic docs: Building with Claude](https://docs.anthropic.com/) · [DeepLearning.AI short courses (free)](https://www.deeplearning.ai/short-courses/)
- **Prompting** — [Anthropic Prompt Engineering overview](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview) · [OpenAI Cookbook](https://cookbook.openai.com/)
- **Concepts** — [Karpathy: Intro to LLMs (1hr talk)](https://www.youtube.com/watch?v=zjkBMFhNj_g) · [Hugging Face LLM Course](https://huggingface.co/learn)
- **Fine-tuning** — [Hugging Face PEFT docs](https://huggingface.co/docs/peft) · [Unsloth (fast LoRA)](https://github.com/unslothai/unsloth)
- **Run open models locally** — [Ollama](https://ollama.com/) · [Hugging Face Models](https://huggingface.co/models)

---

## 🛠️ Phase project
**Build an LLM-powered app** with a real use case (not a chatbot clone): e.g. a document summarizer, a code reviewer, or a structured-data extractor.

**Acceptance criteria:**
- [ ] A **system prompt** that defines role, constraints, and output format.
- [ ] **Structured output** validated against a schema (parsing must fail loudly on bad output).
- [ ] **Error handling** for refusals, `max_tokens` truncation, rate limits, and timeouts.
- [ ] At least one path that uses **streaming** or **tool calling** (your choice, justified).
- [ ] An **eval set of 10+ cases** with pass/fail criteria, runnable as a script that prints a score.
- [ ] **Cost & latency logged** per request (tokens in/out and wall-clock).
- [ ] A short README explaining the prompt design and at least one regression the eval set caught.
- [ ] **Deployed** somewhere reachable (even a simple endpoint or hosted demo).

➡️ Next: [Phase 7 — AI Engineering: RAG & Vector DBs](07-ai-engineering-rag.md)
