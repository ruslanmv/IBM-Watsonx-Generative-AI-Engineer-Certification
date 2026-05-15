# Lab 04 — Retrieval-Augmented Generation

> Exam alignment: **Section 4 — Retrieval-Augmented Generation (17%)** · see `book/chapters/ch04-rag.tex`.

In this lab you build two RAG variants on watsonx.ai:

1. **`01_basic_rag_faiss.py`** — end-to-end in one file: chunk → embed (`ibm/slate-125m-english-rtrvr-v2`) → FAISS → retrieve → generate (`ibm/granite-3-2-8b-instruct`). Perfect for prototypes.
2. **`02_ingest_documents.py` + `app/`** — a production-style application with pluggable retrievers (Chroma or Elasticsearch / watsonx Discovery), a LangChain `RetrievalQA` chain, and a FastAPI + CLI surface (re-used in [`labs/lab-05-deployment`](../lab-05-deployment)).

## What you will build

- A retriever that returns the top-k chunks for a question.
- A grounded prompt that **answers only from the retrieved context** (no hallucinations).
- A FastAPI endpoint `/ask` and a CLI `rag_cli.py` for the same chain.

## Setup

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env       # edit credentials and pick a backend
mkdir -p data && echo "watsonx Discovery uses BM25 + dense vectors over Elasticsearch." > data/note.txt
```

Pick a backend in `.env`:

- `RAG_BACKEND=chroma` — zero-infra, persisted in `./.chroma/`.
- `RAG_BACKEND=elastic` — production-style; set the `ES_*` env vars.

## Run

```bash
# Build the index (one-off; re-run when documents change)
python 02_ingest_documents.py data/

# Ask a question via the CLI
python rag_cli.py "What does watsonx Discovery use under the hood?" --show-sources

# Or run the API
uvicorn server:app --port 8001
curl -s http://localhost:8001/ask -H 'Content-Type: application/json' \
     -d '{"question":"What is watsonx Discovery?"}' | jq
```

For a fully self-contained demo run:

```bash
python 01_basic_rag_faiss.py
```

## Exam-relevant takeaways

- **Chunking is the highest-ROI quality knob**: prefer recursive-character or document-aware splits with 10–20 % overlap.
- **Embeddings**: `ibm/slate-125m-english-rtrvr-v2` (EN) or `ibm/granite-embedding-278m-multilingual` (100+ langs).
- **Vector stores**: FAISS / Chroma for prototypes · watsonx Discovery (Elasticsearch) for governed production.
- **Grounding**: tell the model *“answer only from the context”*. Verify with **Granite Guardian groundedness**.
- **Agentic RAG** = the agent decides when and how to retrieve, possibly multiple times. **AutoRAG** auto-tunes the pipeline.

## Files

| File | What it does |
|---|---|
| `01_basic_rag_faiss.py` | Single-file end-to-end demo (Slate + FAISS) |
| `02_ingest_documents.py` | Chunk + embed + persist into the chosen backend |
| `app/chain.py` | `RetrievalQA` over watsonx LLM + chosen retriever |
| `app/chroma_backend.py` | Local Chroma retriever |
| `app/elastic_backend.py` | Elasticsearch / watsonx Discovery retriever |
| `app/settings.py` | Centralised `pydantic-settings` config |
| `server.py` | FastAPI app exposing `POST /ask` |
| `rag_cli.py` | Same chain from the command line |
| `data/` | Drop your PDFs / text files here |

## Next

Proceed to [`labs/lab-05-deployment`](../lab-05-deployment) to take this app to a Deployment Space.
