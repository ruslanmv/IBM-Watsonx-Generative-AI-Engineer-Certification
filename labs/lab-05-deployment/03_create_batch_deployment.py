"""
Lab 05 · step 3 — Create a Batch Deployment + submit a scoring job.

Batch is for async, latency-tolerant workloads (overnight scoring, large
file transforms). Input + output are object-storage references.

Run:
    python 03_create_batch_deployment.py
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
    client.deployments.ConfigurationMetaNames.NAME: "ticket-classifier-batch",
    client.deployments.ConfigurationMetaNames.BATCH: {},
    client.deployments.ConfigurationMetaNames.HARDWARE_SPEC: {
        "name": os.getenv("HARDWARE_SPEC", "L4-1"),
    },
}
batch_dep = client.deployments.create(
    artifact_uid = os.environ["PROMOTED_ASSET_ID"],
    meta_props   = meta,
)
dep_id = client.deployments.get_id(batch_dep)
print("Batch deployment id:", dep_id)

job = client.deployments.create_job(
    deployment_id = dep_id,
    meta_props={
        client.deployments.ScoringMetaNames.INPUT_DATA_REFERENCES: [{
            "type":     "data_asset",
            "location": {"href": os.environ["BATCH_INPUT_HREF"]},
        }],
        client.deployments.ScoringMetaNames.OUTPUT_DATA_REFERENCE: {
            "type":     "data_asset",
            "location": {"href": os.environ["BATCH_OUTPUT_HREF"]},
        },
    },
)
print("Scoring job submitted:", job)
