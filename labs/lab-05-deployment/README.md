# Lab 05 — Deployment: spaces, endpoints, containers

> Exam alignment: **Section 5 — Deployment (13%)** · see `book/chapters/ch05-deployment.tex`.

In this lab you take the assets you built in labs 02–04 from a **project** to a **Deployment Space**, expose them through an **Online Deployment** and a **Batch Deployment**, and containerise the RAG service from lab 04.

## What you will build

1. A new Deployment Space (Dev).
2. A promoted **prompt template** (lab 02) + an **Online Deployment** that apps call via REST.
3. A **Batch Deployment** that scores a CSV from object storage.
4. A Docker image of the lab-04 RAG service — ready for any container runtime.

## Setup

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env       # paste credentials + your existing prompt asset ID
```

## Run

```bash
python 01_promote_prompt_template.py        # copy asset into a Space
python 02_create_online_deployment.py       # create POST /text/generation endpoint
python 03_create_batch_deployment.py        # create batch job endpoint
```

Containerise the lab-04 RAG service:

```bash
cd ../lab-04-rag
docker build -f ../lab-05-deployment/Dockerfile -t cert-rag:dev .
docker run --rm -p 8001:8001 --env-file .env cert-rag:dev
curl -s http://localhost:8001/ask -H 'Content-Type: application/json' \
     -d '{"question":"What is watsonx Discovery?"}' | jq
```

## Exam-relevant takeaways

- A **Project** is for *build*. A **Deployment Space** is for *promote + serve*.
- Every promote creates an **immutable version**. Rollback = re-deploy the previous version.
- **Online** = sync REST endpoint (latency-bound). **Batch** = async job over a dataset → results to Cloud Object Storage.
- Recognise the **Model Gateway**: a single URL fronting many backing models with central rate-limit and A/B.
- Refresh RAG corpora with **watsonx AI Pipelines**.

## Files

| File | What it does |
|---|---|
| `01_promote_prompt_template.py` | Move an asset from project → space |
| `02_create_online_deployment.py` | Create an online deployment (REST endpoint) |
| `03_create_batch_deployment.py` | Create a batch deployment + submit a scoring job |
| `Dockerfile` | Image for the lab-04 RAG service |
| `.dockerignore` | Exclude venvs / build artefacts |
| `.env.example`, `requirements.txt` | Setup |

## Next

Proceed to [`labs/lab-06-integration`](../lab-06-integration) for LangChain agents and MCP.
