"""
Lab 03 · step 3 — Evaluate the tuned model vs the few-shot baseline.

Reads the held-out test split, runs each example through (a) the few-shot
baseline on the un-tuned base model, and (b) the deployed tuned model, and
prints accuracy + F1 per class. Replace TUNED_DEPLOYMENT_ID with the ID
from your completed tuning run.

Run:
    python 03_evaluate_tuned_model.py
"""
import json
import os
from collections import Counter
from pathlib import Path
from dotenv import load_dotenv
from ibm_watsonx_ai import APIClient, Credentials
from ibm_watsonx_ai.foundation_models import ModelInference
from ibm_watsonx_ai.metanames import GenTextParamsMetaNames as GenParams
from sklearn.metrics import accuracy_score, classification_report

load_dotenv()
client = APIClient(
    Credentials(url=os.environ["WATSONX_URL"], api_key=os.environ["WATSONX_APIKEY"]),
    project_id=os.environ["WATSONX_PROJECT_ID"],
)

FEW_SHOT_PREAMBLE = (
    "Categorise the support ticket as BILLING, TECH, or OTHER. Reply with one word.\n\n"
    "Ticket: My charge is wrong\nCategory: BILLING\n\n"
    "Ticket: The app keeps crashing\nCategory: TECH\n\n"
    "Ticket: I cannot reset my password\nCategory: TECH\n\n"
)

base = ModelInference(
    model_id=os.getenv("BASE_MODEL_ID", "ibm/granite-3-2-8b-instruct"),
    api_client=client,
    params={GenParams.DECODING_METHOD: "greedy", GenParams.MAX_NEW_TOKENS: 6,
            GenParams.STOP_SEQUENCES: ["\n"]},
)

TUNED_DEPLOYMENT_ID = os.getenv("TUNED_DEPLOYMENT_ID")
if TUNED_DEPLOYMENT_ID:
    tuned = ModelInference(
        deployment_id=TUNED_DEPLOYMENT_ID,
        api_client=client,
        params={GenParams.DECODING_METHOD: "greedy", GenParams.MAX_NEW_TOKENS: 6,
                GenParams.STOP_SEQUENCES: ["\n"]},
    )
else:
    tuned = None
    print("TUNED_DEPLOYMENT_ID not set — will evaluate the baseline only.")

test_path = Path(os.getenv("DATA_DIR", "./dataset-prep")) / "test.jsonl"
rows = [json.loads(line) for line in test_path.read_text().splitlines() if line.strip()]
print(f"Loaded {len(rows)} test rows. Class balance:",
      Counter(r["output"] for r in rows))

def classify(model, ticket_prompt):
    raw = model.generate_text(ticket_prompt).strip().split("\n")[0].upper()
    for label in ("BILLING", "TECH", "OTHER"):
        if label in raw:
            return label
    return "OTHER"

y_true       = [r["output"] for r in rows]
y_baseline   = [classify(base, FEW_SHOT_PREAMBLE + r["input"]) for r in rows]
print("\nFEW-SHOT BASELINE")
print("  accuracy:", accuracy_score(y_true, y_baseline))
print(classification_report(y_true, y_baseline, digits=3))

if tuned:
    y_tuned = [classify(tuned, r["input"]) for r in rows]
    print("\nTUNED MODEL")
    print("  accuracy:", accuracy_score(y_true, y_tuned))
    print(classification_report(y_true, y_tuned, digits=3))
