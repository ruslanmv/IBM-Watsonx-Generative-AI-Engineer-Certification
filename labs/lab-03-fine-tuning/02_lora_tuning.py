"""
Lab 03 · step 2 — Launch a LoRA fine-tuning job on watsonx Tuning Studio.

This script:
  1. Uploads the train/val JSONL splits as project data assets.
  2. Creates a TuneExperiment with method='lora' on the configured base model.
  3. Submits the run and prints the job ID.

Notes on hyperparameters:
  - rank (r) = 8           controls adapter capacity (4..32 in practice)
  - alpha   = 16           effective scale = (alpha / r) * BA
  - lr      = 2e-4         too high -> divergence; too low -> nothing learned
  - epochs  = 3            more than ~5 usually overfits on small data

Run:
    python 02_lora_tuning.py
"""
import os
from pathlib import Path
from dotenv import load_dotenv
from ibm_watsonx_ai import APIClient, Credentials
from ibm_watsonx_ai.foundation_models import TuneExperiment

load_dotenv()
client = APIClient(
    Credentials(url=os.environ["WATSONX_URL"], api_key=os.environ["WATSONX_APIKEY"]),
    project_id=os.environ["WATSONX_PROJECT_ID"],
)

data_dir = Path(os.getenv("DATA_DIR", "./dataset-prep"))
base_model = os.getenv("BASE_MODEL_ID", "ibm/granite-3-2-8b-instruct")

# Upload the JSONL splits as project assets
def upload(path: Path) -> str:
    print(f"Uploading {path.name} ...")
    asset = client.data_assets.create(name=path.name, file_path=str(path))
    return client.data_assets.get_id(asset)

train_id = upload(data_dir / "train.jsonl")
val_id   = upload(data_dir / "val.jsonl")

# Configure + launch the LoRA tune
tune = TuneExperiment(client)
job = tune.run(
    name              = "ticket-classifier-lora-v1",
    base_model        = base_model,
    task_type         = "classification",
    training_data     = train_id,
    validation_data   = val_id,
    method            = {"type": "lora", "rank": 8, "alpha": 16, "dropout": 0.05},
    hyperparameters   = {"learning_rate": 2e-4, "num_epochs": 3, "batch_size": 16},
    auto_update_model = False,
)
print("\nTuning job submitted.")
print("  job id:", job.id)
print("  state :", job.state)
print("\nWatch progress in watsonx.ai Studio → Tuning Studio.")
