"""
Lab 01 · step 2 — Inspect the foundation-model catalogue.

Prints the model_id, label, billing tier, and max input/output sequence
length for every chat/instruct/embedding model your watsonx.ai instance
can see.

Run:
    python 02_list_models.py

Exam hint:
  - The default IBM instruct model is ibm/granite-3-2-8b-instruct.
  - Pick the smallest Granite that meets the quality bar; jump to
    meta-llama/llama-3-3-70b-instruct only when long-context or
    multilingual reasoning is required.
"""
import os
from dotenv import load_dotenv
from ibm_watsonx_ai import APIClient, Credentials

load_dotenv()
client = APIClient(
    Credentials(url=os.environ["WATSONX_URL"], api_key=os.environ["WATSONX_APIKEY"]),
    project_id=os.environ["WATSONX_PROJECT_ID"],
)

resources = client.foundation_models.get_model_specs().get("resources", [])
print(f"Found {len(resources)} models in the catalogue.\n")
print(f"{'MODEL_ID':<48}  {'TIER':<10}  {'MAX_SEQ':>8}  LABEL")
print("-" * 110)
for r in resources:
    mid    = r.get("model_id", "")
    tier   = r.get("tier") or r.get("functions", [{}])[0].get("id", "")
    label  = r.get("label", "")
    limits = r.get("model_limits") or {}
    max_seq = limits.get("max_sequence_length") or limits.get("max_output_tokens") or ""
    print(f"{mid:<48}  {str(tier):<10}  {str(max_seq):>8}  {label}")
