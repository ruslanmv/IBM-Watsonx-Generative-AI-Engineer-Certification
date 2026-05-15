"""FastAPI endpoint exposing the RAG chain at POST /ask.

Run:
    uvicorn server:app --port 8001 --reload

Then:
    curl -s http://localhost:8001/ask -H 'Content-Type: application/json' \
         -d '{"question":"What is watsonx Discovery?"}' | jq
"""
from fastapi import FastAPI
from pydantic import BaseModel

from app.chain import build_chain

app = FastAPI(title="Lab 04 — Grounded RAG")
qa = build_chain()


class Ask(BaseModel):
    question: str
    k: int | None = None


@app.get("/healthz")
def healthz():
    return {"ok": True}


@app.post("/ask")
def ask(body: Ask):
    if body.k:
        qa.retriever.search_kwargs["k"] = body.k
    result = qa.invoke({"query": body.question})
    return {
        "answer": result.get("result"),
        "sources": [
            {"metadata": dict(d.metadata or {}),
             "text": d.page_content[:500]}
            for d in result.get("source_documents", [])
        ],
    }
