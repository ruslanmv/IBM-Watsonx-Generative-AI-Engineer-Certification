"""
Lab 02 · step 2 — Parameter sweep.

For a fixed summarisation prompt, sweep temperature × top_p with both
greedy and sampling decoding. Print one output per cell so you can eyeball
the quality / determinism trade-off.

Run:
    python 02_parameter_sweep.py
"""
import itertools
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

ARTICLE = (
    "watsonx Discovery is IBM's managed hybrid retrieval service. It combines "
    "BM25 keyword search with dense-vector search over the same Elasticsearch "
    "index, then optionally re-ranks the top results with a cross-encoder. "
    "It integrates with watsonx.governance for lineage and drift monitoring."
)
PROMPT = f"Summarise in two short bullets:\n\n{ARTICLE}"

MODEL = os.getenv("LLM_MODEL_ID", "ibm/granite-3-2-8b-instruct")
TEMPS  = [0.0, 0.4, 0.8]
TOP_PS = [0.5, 0.9]
DECODINGS = ["greedy", "sample"]

for decoding, temp, top_p in itertools.product(DECODINGS, TEMPS, TOP_PS):
    params = {
        GenParams.DECODING_METHOD: decoding,
        GenParams.MAX_NEW_TOKENS: 80,
        GenParams.TEMPERATURE: temp,
        GenParams.TOP_P: top_p,
        GenParams.RANDOM_SEED: 42,
    }
    model = ModelInference(model_id=MODEL, api_client=client, params=params)
    out = model.generate_text(PROMPT).strip().replace("\n", " ")[:120]
    print(f"decoding={decoding:<6} temp={temp:<3}  top_p={top_p}  | {out}")
