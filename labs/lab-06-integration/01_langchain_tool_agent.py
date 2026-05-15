"""
Lab 06 · step 1 — Tool-calling agent on watsonx.

Granite 3.x supports native tool calling. We define three Python tools
(account lookup, knowledge-base search, email draft), give them to a
ChatWatsonx model, and let the agent decide which to call.

Run:
    python 01_langchain_tool_agent.py
"""
import os
from dotenv import load_dotenv
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.tools import tool
from langchain_ibm import ChatWatsonx

load_dotenv()

# ---- 1) Tools the agent may call -------------------------------------------
ACCOUNTS = {
    "882": {"name": "ACME GmbH", "tier": "enterprise", "status": "active"},
    "123": {"name": "Globex Ltd", "tier": "standard",  "status": "suspended"},
}
KB = {
    "refund":  "Enterprise customers may request a pro-rated refund within 30 days.",
    "outage":  "Outages over the SLA threshold trigger an automatic credit.",
    "hours":   "Premium support operates 24/7. Standard support is 9-17 CET.",
}

@tool
def lookup_account(account_id: str) -> dict:
    """Return account name, tier, and status for the given account ID."""
    return ACCOUNTS.get(account_id, {"error": "account not found"})

@tool
def search_kb(topic: str) -> str:
    """Look up a short policy text by topic keyword (refund / outage / hours)."""
    return KB.get(topic.lower(), "no matching entry")

@tool
def draft_email(to: str, subject: str, body: str) -> str:
    """Compose a polite customer email and return the rendered draft."""
    return (f"To: {to}\nSubject: {subject}\n\nDear customer,\n\n{body}\n\n"
            "Kind regards,\nACME Customer Care")

# ---- 2) ChatWatsonx LLM ----------------------------------------------------
llm = ChatWatsonx(
    model_id   = os.getenv("LLM_MODEL_ID", "ibm/granite-3-2-8b-instruct"),
    url        = os.environ["WATSONX_URL"],
    apikey     = os.environ["WATSONX_APIKEY"],
    project_id = os.environ["WATSONX_PROJECT_ID"],
    params={"temperature": 0.2, "max_new_tokens": 400},
)

# ---- 3) Agent --------------------------------------------------------------
prompt = ChatPromptTemplate.from_messages([
    ("system",
     "You are a senior customer-care agent at ACME. Use the tools provided. "
     "Cite which tools you used. If you cannot help, say so honestly."),
    ("human",       "{input}"),
    ("placeholder", "{agent_scratchpad}"),
])
agent    = create_tool_calling_agent(llm, [lookup_account, search_kb, draft_email], prompt)
executor = AgentExecutor(
    agent  = agent,
    tools  = [lookup_account, search_kb, draft_email],
    verbose=True,
)

print(executor.invoke({
    "input": "Account 882 reports an outage. Summarise their status "
             "and draft a short reply quoting our outage policy.",
})["output"])
