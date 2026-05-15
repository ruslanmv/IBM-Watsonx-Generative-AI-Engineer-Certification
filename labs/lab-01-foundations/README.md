# Lab 01 — Foundations: Your first watsonx.ai call

> Exam alignment: **Section 1 — Analyze and Design a Generative AI Solution (15%)** · see `book/chapters/ch01-foundations.tex`.

In this lab you connect to watsonx.ai, list the available foundation models, and demonstrate the **five core capabilities** the exam tests: Summarization, Classification, Generation (text + code + translation), Extraction, and Q&A.

## What you will build

1. A working watsonx.ai client (credentials + project).
2. A catalogue listing showing model IDs, billing classes, and context windows.
3. A short capability demo — one prompt per capability — against `ibm/granite-3-2-8b-instruct`.

## Prerequisites

- IBM Cloud account with a watsonx.ai service (free tier OK).
- A **project** created in watsonx.ai (Studio → Projects → New project).
- API key with at least *Reader* role on the watsonx service.
- Python 3.10+.

## Setup

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env       # then edit and paste your credentials
```

Minimum `.env`:

```
WATSONX_URL=https://us-south.ml.cloud.ibm.com
WATSONX_APIKEY=__paste_your_key__
WATSONX_PROJECT_ID=__paste_your_project_id__
```

## Run

```bash
python 01_first_prompt.py        # hello world: generate_text + chat
python 02_list_models.py         # the watsonx catalogue
python 03_capability_demo.py     # five capabilities in one script
```

Expected output (truncated):

```
[01] generate_text: "Quantum computing uses qubits ..."
[02] model_id=ibm/granite-3-2-8b-instruct  tier=class_2  max_seq=131072
[03] SUMMARY: Three bullets ...
     CLASSIFY: BILLING
     GENERATE: def fibonacci(n): ...
     EXTRACT:  {"name": "ACME", "amount": 482.50, "date": "2026-03-14"}
     QA:       The capital of France is Paris.
```

## Exam-relevant takeaways

- The default IBM-native instruct model in 2026 is **`ibm/granite-3-2-8b-instruct`** — pick it when the question says *IBM-native, English, enterprise*.
- The five capabilities are not arbitrary; the exam asks you to map a business problem to exactly one of them.
- Every model has a billing class (Class 1–13). The cheapest correct answer almost always uses a smaller Granite or an embedding model.

## Files

| File | What it does |
|---|---|
| `01_first_prompt.py` | Authenticate, generate text, stream a chat |
| `02_list_models.py` | Inspect the model catalogue (IDs, classes, limits) |
| `03_capability_demo.py` | One prompt per capability, side by side |
| `.env.example` | Credentials template — copy to `.env` |
| `requirements.txt` | Minimum dependencies |

## Next

Move on to [`labs/lab-02-prompt-engineering`](../lab-02-prompt-engineering) to drill prompt design and parameter tuning.
