"""
Lab 02 · step 1 — Zero-shot vs few-shot vs chain-of-thought.

We ask Granite to classify a customer ticket three ways and compare the
outputs. The exam frequently shows you a prompt and asks which style it is.

Run:
    python 01_zero_few_shot.py
"""
import os
from dotenv import load_dotenv
from ibm_watsonx_ai import APIClient, Credentials
from ibm_watsonx_ai.foundation_models import ModelInference
from ibm_watsonx_ai.metanames import GenTextParamsMetaNames as GenParams

load_dotenv()
client = APIClient(
    Credentials(url=os.environ["WATSONX_URL"], api_key=os.environ["WATSONX_APIKEY"]),
    project_id=os.environ["WATSONX_PROJECT_ID"],
)
model = ModelInference(
    model_id=os.getenv("LLM_MODEL_ID", "ibm/granite-3-2-8b-instruct"),
    api_client=client,
    params={
        GenParams.DECODING_METHOD: "greedy",
        GenParams.MAX_NEW_TOKENS: 60,
        GenParams.STOP_SEQUENCES: ["\n\n"],
    },
)

TICKET = "Setup wizard works but the app freezes when I open the payments tab."

ZERO_SHOT = (
    "Classify the ticket as BILLING, TECH, or OTHER. Reply with one word.\n"
    f"Ticket: {TICKET}\nCategory:"
)

FEW_SHOT = (
    "Classify the ticket as BILLING, TECH, or OTHER. Reply with one word.\n\n"
    "Ticket: My charge is wrong\nCategory: BILLING\n\n"
    "Ticket: The app keeps crashing\nCategory: TECH\n\n"
    "Ticket: I cannot reset my password\nCategory: TECH\n\n"
    f"Ticket: {TICKET}\nCategory:"
)

COT = (
    "Classify the ticket as BILLING, TECH, or OTHER. "
    "First, reason in one short sentence; then reply on a new line with 'Category: <LABEL>'.\n"
    f"Ticket: {TICKET}\nReasoning:"
)

for name, prompt in [("ZERO-SHOT", ZERO_SHOT), ("FEW-SHOT", FEW_SHOT), ("CoT", COT)]:
    print(f"\n===== {name} =====")
    print(model.generate_text(prompt).strip())
