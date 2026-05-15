"""
Lab 01 · step 3 — The five capabilities in one script.

For each of Summarization, Classification, Generation (text+code+translation),
Extraction, and Q&A, we run a tiny prompt against ibm/granite-3-2-8b-instruct
and print the result. Compare the outputs side by side — this is the mental
model the exam expects you to use.
"""
import json
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
    params={GenParams.DECODING_METHOD: "greedy", GenParams.MAX_NEW_TOKENS: 200},
)

ARTICLE = (
    "watsonx.ai is IBM's enterprise studio for foundation models. It includes "
    "Prompt Lab for experimentation, Tuning Studio for parameter-efficient "
    "fine-tuning such as LoRA, and a model gateway for routing inference "
    "across multiple providers. Models include the open-weight IBM Granite "
    "family, Meta Llama 3.3, and Mistral."
)
TICKET   = "The app crashes every time I open the payments tab on iOS 17."
INVOICE  = "Invoice #4421 from ACME GmbH for 482.50 EUR was issued on 2026-03-14."
QUESTION = "What is the capital of France?"

CAPS = {
    "SUMMARIZE":  f"Summarize the following text in three short bullets:\n\n{ARTICLE}",
    "CLASSIFY":   ("Classify the ticket as BILLING, TECH, or OTHER. Reply with one word.\n"
                   f"Ticket: {TICKET}\nCategory:"),
    "GENERATE_CODE": "Write a Python function fibonacci(n) that returns the n-th Fibonacci number.",
    "TRANSLATE":  "Translate to French. Reply with only the translation: 'Restart the router.'",
    "EXTRACT":    ("Extract vendor, amount, currency, and date as JSON. "
                   f"No prose, just JSON.\n\n{INVOICE}"),
    "QA":         f"Answer in one short sentence: {QUESTION}",
}

for name, prompt in CAPS.items():
    out = model.generate_text(prompt).strip()
    print(f"\n----- {name} -----")
    print(out)
