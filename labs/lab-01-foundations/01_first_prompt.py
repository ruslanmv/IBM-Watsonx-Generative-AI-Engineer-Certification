"""
Lab 01 · step 1 — Your first watsonx.ai call.

Demonstrates:
  - authenticating with IBM Cloud (API key + project ID)
  - a synchronous text generation
  - a streaming chat call

Run:
    python 01_first_prompt.py
"""
import os
from dotenv import load_dotenv
from ibm_watsonx_ai import APIClient, Credentials
from ibm_watsonx_ai.foundation_models import ModelInference
from ibm_watsonx_ai.metanames import GenTextParamsMetaNames as GenParams

load_dotenv()

creds = Credentials(
    url=os.environ["WATSONX_URL"],
    api_key=os.environ["WATSONX_APIKEY"],
)
client = APIClient(creds, project_id=os.environ["WATSONX_PROJECT_ID"])

model_id = os.getenv("LLM_MODEL_ID", "ibm/granite-3-2-8b-instruct")
params = {
    GenParams.DECODING_METHOD: "greedy",
    GenParams.MAX_NEW_TOKENS: int(os.getenv("LLM_MAX_NEW_TOKENS", 256)),
    GenParams.TEMPERATURE: float(os.getenv("LLM_TEMPERATURE", 0.2)),
}

model = ModelInference(model_id=model_id, api_client=client, params=params)

# ---- 1) generate_text -------------------------------------------------------
prompt = "Explain quantum computing in two sentences for a high-school student."
out = model.generate_text(prompt)
print("\n[01] generate_text >")
print(out.strip())

# ---- 2) chat with streaming --------------------------------------------------
messages = [
    {"role": "system", "content": "You are a friendly IT helpdesk agent."},
    {"role": "user",   "content": "My laptop will not connect to the office Wi-Fi."},
]
print("\n[02] chat_stream >")
for chunk in model.chat_stream(messages=messages):
    delta = chunk.get("choices", [{}])[0].get("delta", {}).get("content", "")
    print(delta, end="", flush=True)
print()
