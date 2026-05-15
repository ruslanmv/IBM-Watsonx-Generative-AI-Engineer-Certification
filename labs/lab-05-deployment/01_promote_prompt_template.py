"""
Lab 05 · step 1 — Promote a prompt-template asset from a Project to a Space.

Projects are for build. Spaces are for serve. The promote step creates a new
immutable version of the asset inside the target Space; applications then
call the Space, not the Project.

Run:
    python 01_promote_prompt_template.py
"""
import os
from dotenv import load_dotenv
from ibm_watsonx_ai import APIClient, Credentials

load_dotenv()
client = APIClient(
    Credentials(url=os.environ["WATSONX_URL"], api_key=os.environ["WATSONX_APIKEY"]),
    project_id=os.environ["WATSONX_PROJECT_ID"],
)

promoted = client.repository.promote_asset(
    asset_id        = os.environ["PROMPT_ASSET_ID"],
    target_space_id = os.environ["WATSONX_SPACE_ID"],
)
asset_id = promoted["metadata"]["asset_id"]
print("Promoted asset_id (in space):", asset_id)
print("Save this for the next step  ->  export PROMOTED_ASSET_ID=" + asset_id)
