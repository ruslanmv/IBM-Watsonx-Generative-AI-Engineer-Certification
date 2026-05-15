"""
Lab 06 · step 2 — Router chain.

A small classifier prompt picks one of N specialist prompts, saving cost
by keeping easy questions away from the largest model.

Run:
    python 02_router_chain.py
"""
import os
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ibm import ChatWatsonx

load_dotenv()
llm = ChatWatsonx(
    model_id   = os.getenv("LLM_MODEL_ID", "ibm/granite-3-2-8b-instruct"),
    url        = os.environ["WATSONX_URL"],
    apikey     = os.environ["WATSONX_APIKEY"],
    project_id = os.environ["WATSONX_PROJECT_ID"],
    params={"temperature": 0.0, "max_new_tokens": 200},
)

ROUTER_PROMPT = ChatPromptTemplate.from_messages([
    ("system", "Classify the user request into exactly one of: BILLING, TECH, OTHER. "
               "Reply with one word only."),
    ("user",   "{q}"),
])

BILLING_PROMPT = ChatPromptTemplate.from_messages([
    ("system", "You are a polite billing specialist. Reference the invoice number if present."),
    ("user",   "{q}"),
])
TECH_PROMPT = ChatPromptTemplate.from_messages([
    ("system", "You are a senior tech-support engineer. Ask one clarifying question if needed, "
               "otherwise provide step-by-step troubleshooting."),
    ("user",   "{q}"),
])
OTHER_PROMPT = ChatPromptTemplate.from_messages([
    ("system", "You are a courteous generalist. Acknowledge the request and offer to escalate "
               "to the right team."),
    ("user",   "{q}"),
])

router = ROUTER_PROMPT  | llm | StrOutputParser()
billing = BILLING_PROMPT | llm | StrOutputParser()
tech    = TECH_PROMPT    | llm | StrOutputParser()
other   = OTHER_PROMPT   | llm | StrOutputParser()

def ask(q: str) -> str:
    label = router.invoke({"q": q}).strip().upper()
    chain = {"BILLING": billing, "TECH": tech}.get(label, other)
    return f"[{label}]\n{chain.invoke({'q': q})}"

for q in [
    "Invoice 4421 shows the wrong VAT rate.",
    "My laptop will not connect to the office Wi-Fi.",
    "Do you have a French version of your docs?",
]:
    print("\nQ:", q)
    print(ask(q))
