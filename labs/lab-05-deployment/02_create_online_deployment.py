"""
Lab 05 · step 2 — Create an Online Deployment for the promoted asset.

Produces a stable HTTPS endpoint your applications can POST to. Set the
hardware profile to match the model size (e.g. L4-1 for a Granite 8B, A100
for a 70B).

Run:
    python 02_create_online_deployment.py
"""
import os
from dotenv import load_dotenv
from ibm_watsonx_ai import APIClient, Credentials

load_dotenv()
client = APIClient(
    Credentials(url=os.environ["WATSONX_URL"], api_key=os.environ["WATSONX_APIKEY"]),
    space_id=os.environ["WATSONX_SPACE_ID"],
)

meta = {
    client.deployments.ConfigurationMetaNames.NAME:
        "ticket-classifier-online",
    client.deployments.ConfigurationMetaNames.DESCRIPTION:
        "Online deployment of the LoRA-tuned Granite 3.2 8B ticket classifier.",
    client.deployments.ConfigurationMetaNames.ONLINE: {},
    client.deployments.ConfigurationMetaNames.HARDWARE_SPEC: {
        "name": os.getenv("HARDWARE_SPEC", "L4-1"),
    },
}

deployment = client.deployments.create(
    artifact_uid = os.environ["PROMOTED_ASSET_ID"],
    meta_props   = meta,
)
print("Online deployment created.")
print("  id  :", client.deployments.get_id(deployment))
print("  href:", client.deployments.get_href(deployment))
print("\nCall it from any language with:")
print("  POST {url}/ml/v1/deployments/{id}/text/generation")
