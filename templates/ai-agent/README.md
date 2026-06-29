# AI Agent (starter)

The entire idea of an agent in ~80 lines: **an LLM running in a `while` loop with tools.** The model decides which tool to call, your code runs it and feeds the result back, repeat until it answers. No framework — so you actually understand what LangGraph/CrewAI do for you. Pairs with [Module 8](../../phases/08-agents.md).

## Run

```bash
pip install -r requirements.txt
export ANTHROPIC_API_KEY=sk-ant-...
python agent.py "What is 24 * 7 + 100, and what files are in this folder?"
```

You'll see each step print the tool call and result, then the final answer.

## What this demonstrates
- **Tool calling end-to-end**: schema → model emits a `tool_use` → you execute → return `tool_result` → loop.
- The three things every agent needs: **tool dispatch**, a **stop condition**, and a **step limit** (no runaway cost).
- The model never runs your code — it *asks*; you own execution, security, and side effects.

## ⚠️ Safety note
The demo `calculator` uses `eval` behind a character allowlist for brevity. **Never** expose unsandboxed `eval`/shell/file-write tools to an agent in anything real — tool outputs can carry prompt injection, and the model can be steered into destructive calls. Sandbox, allowlist, and require confirmation for destructive actions.

## Make it yours (upgrade path → portfolio piece)
1. Add a **real** tool: web search, an HTTP API, a DB query, your RAG retriever from `../rag-app`.
2. Add retries, timeouts, and a per-run cost cap.
3. Add **tracing** (Langfuse/LangSmith) so you can see each step's latency + cost.
4. Build an **eval set** of tasks with known answers; measure task success rate.
5. Expose one of your tools over **MCP**, or graduate the loop to **LangGraph** for branching/multi-agent.
