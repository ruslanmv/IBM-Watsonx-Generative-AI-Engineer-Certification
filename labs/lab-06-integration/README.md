# Lab 06 — Integration &amp; Orchestration

> Exam alignment: **Section 6 — watsonx Integration and Model Orchestration (8%)** · see `book/chapters/ch06-integration.tex`.

In this lab you wire watsonx.ai into LangChain agents, build a router chain, and stand up a minimal **Model Context Protocol (MCP)** server the agent calls as a tool.

## What you will build

1. A **tool-calling agent** using `ChatWatsonx` and `create_tool_calling_agent` — the modern way to give an LLM access to functions.
2. A **router chain** that classifies the request first, then dispatches to the right specialist prompt.
3. A small **MCP server** that exposes a tool (“check account status”), and a client that calls it from an agent.

## Setup

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

## Run

```bash
python 01_langchain_tool_agent.py   # ChatWatsonx + tool-calling AgentExecutor
python 02_router_chain.py           # classify -> dispatch -> respond
python 03_mcp_server_demo.py        # tiny MCP server (run in another terminal)
python 03_mcp_client_demo.py        # an agent that calls the MCP tool
```

## Exam-relevant takeaways

- LangChain core building blocks: **LLM / ChatWatsonx, Prompt, Chain, Tool, Agent, Memory, Retriever, Output Parser**.
- Granite 3.x, Llama 3.3 and Mistral all support **native tool calling** — prefer `create_tool_calling_agent` over the legacy ReAct text-only agent.
- **Router chain** = cheap classifier in front of N specialists. Saves cost without sacrificing quality.
- **MCP (Model Context Protocol)** is the open, vendor-neutral protocol for exposing tools + data to LLM apps and IDEs.

## Files

| File | What it does |
|---|---|
| `01_langchain_tool_agent.py` | Granite chat + 3 custom Python tools + AgentExecutor |
| `02_router_chain.py` | Classifier prompt routing to specialist prompts |
| `03_mcp_server_demo.py` | Minimal MCP server exposing one tool |
| `03_mcp_client_demo.py` | An agent that lists and calls MCP tools |
| `.env.example`, `requirements.txt` | Setup |

You are done with the hands-on labs. Head to `book/chapters/appendix-b-mock-exam.tex` and try the mock exam.
