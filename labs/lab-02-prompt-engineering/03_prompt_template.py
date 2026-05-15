"""
Lab 02 · step 3 — Versioned prompt templates.

Stores a named, variable-driven prompt asset in your watsonx project, then
loads it back and runs an inference. Treat templates like source code:
name, version, promote, monitor.

Run:
    python 03_prompt_template.py
"""
import os
from dotenv import load_dotenv
from ibm_watsonx_ai import Credentials
from ibm_watsonx_ai.foundation_models.prompts import (
    PromptTemplate,
    PromptTemplateManager,
)

load_dotenv()
creds = Credentials(
    url=os.environ["WATSONX_URL"],
    api_key=os.environ["WATSONX_APIKEY"],
)
ptm = PromptTemplateManager(
    credentials=creds,
    project_id=os.environ["WATSONX_PROJECT_ID"],
)

template = PromptTemplate(
    name="ticket-classifier-v1",
    description="Categorise support tickets into BILLING / TECH / OTHER.",
    input_variables=["ticket_text"],
    input_text=("Categorise the support ticket below.\n"
                "Ticket: {ticket_text}\nCategory:"),
    examples=[
        ["My charge is wrong",     "BILLING"],
        ["The app keeps crashing", "TECH"],
    ],
    model_id=os.getenv("LLM_MODEL_ID", "ibm/granite-3-2-8b-instruct"),
    model_params={"decoding_method": "greedy", "max_new_tokens": 6,
                  "stop_sequences": ["\n"]},
)
stored = ptm.store_prompt(template)
print("Stored prompt asset:", stored.prompt_id)

# Load + run via the SDK
prompt_text = ptm.load_prompt(stored.prompt_id).input_text
rendered = prompt_text.format(ticket_text="I cannot log in to the mobile app")
print("\nRendered prompt:\n", rendered)

# (Optional) tear-down
# ptm.delete_prompt(stored.prompt_id)
