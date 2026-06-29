# Phase 8 — AI Agents & Agentic Systems

**Goal:** Build LLM systems that can use tools, take actions, and accomplish multi-step goals autonomously. The frontier of AI engineering in 2026.
**Time:** 3–4 weeks.

---

## 🎯 Outcomes
You can design and build reliable agents with tool use, memory, and orchestration — and know how to keep them from going off the rails.

## ✅ Checklist

### Agent fundamentals
- [ ] What makes something an "agent" (LLM + tools + loop + goal)
- [ ] Tool / function calling
- [ ] The ReAct pattern (reason + act)
- [ ] Planning & task decomposition
- [ ] Memory: short-term (context) vs long-term (vector store)
- [ ] Reflection & self-correction loops

### Building agents
- [ ] Single-agent tool-use loops
- [ ] Multi-agent systems (orchestrator + workers)
- [ ] Human-in-the-loop & approvals
- [ ] **[Model Context Protocol (MCP)](https://modelcontextprotocol.io/)** — the standard for tool/data connections
- [ ] Guardrails, retries, error recovery
- [ ] Cost & loop control (don't let agents run forever)

### Frameworks & tools
- [ ] [LangGraph](https://www.langchain.com/langgraph) (graph-based agent orchestration)
- [ ] [Anthropic Claude Agent SDK](https://docs.anthropic.com/) / OpenAI Agents SDK
- [ ] [CrewAI](https://www.crewai.com/) / [AutoGen](https://microsoft.github.io/autogen/) (awareness)
- [ ] Observability: [LangSmith](https://www.langchain.com/langsmith), [Langfuse](https://langfuse.com/)

### Evaluation & safety
- [ ] Evaluating agent task success
- [ ] Tracing & debugging agent runs
- [ ] Prompt injection & tool-use security
- [ ] Sandboxing dangerous tools

## 📚 Best resources
- **Must-read** — [Anthropic: Building Effective Agents](https://www.anthropic.com/research/building-effective-agents) **(the best guide, start here)**
- **Courses** — [DeepLearning.AI: AI Agents short courses](https://www.deeplearning.ai/short-courses/) · [LangGraph tutorials](https://langchain-ai.github.io/langgraph/tutorials/)
- **MCP** — [Model Context Protocol docs](https://modelcontextprotocol.io/) + [example servers](https://github.com/modelcontextprotocol/servers)
- **roadmap.sh** — [AI Agents Roadmap](https://roadmap.sh/ai-agents)

## 🛠️ Phase project
**Build a useful agent** that does real work: e.g. a research agent (search → read → synthesize → cite), a coding agent, or a customer-support agent with tools. Must have: tool calling, error handling, loop limits, and a trace/eval showing it succeeds on a test set. Bonus: expose a tool via MCP.

➡️ Next: [Phase 9 — MLOps & Production](09-mlops-production.md)
