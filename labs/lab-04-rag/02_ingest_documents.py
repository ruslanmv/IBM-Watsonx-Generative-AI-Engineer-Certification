"""
Lab 04 · step 2 — Ingest documents into the configured RAG backend.

Reads everything under the given directory, chunks it, embeds the chunks
with the configured embedder, and writes them into Chroma or Elasticsearch
(based on RAG_BACKEND). Re-run any time the source corpus changes.

Usage:
    python 02_ingest_documents.py data/
"""
import glob
import sys
from pathlib import Path
from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader, PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings

load_dotenv()
from app.settings import settings

src = Path(sys.argv[1] if len(sys.argv) > 1 else "./data")
if not src.exists():
    raise SystemExit(f"Source directory {src} does not exist")

docs = []
for path in glob.glob(str(src / "**/*"), recursive=True):
    if path.endswith(".pdf"):
        docs.extend(PyPDFLoader(path).load())
    elif path.endswith((".txt", ".md")):
        docs.extend(TextLoader(path, encoding="utf-8").load())
print(f"Loaded {len(docs)} document(s) from {src}")

splitter = RecursiveCharacterTextSplitter(chunk_size=512, chunk_overlap=64)
chunks = splitter.split_documents(docs)
print(f"Produced {len(chunks)} chunk(s)")

embeddings = HuggingFaceEmbeddings(model_name=settings.EMBEDDINGS_MODEL)

if settings.RAG_BACKEND.lower() == "chroma":
    from langchain_chroma import Chroma
    Chroma.from_documents(
        chunks, embedding=embeddings,
        collection_name="kb", persist_directory=settings.CHROMA_DIR,
    )
    print(f"Indexed into Chroma at {settings.CHROMA_DIR}")
else:
    import os
    from elasticsearch import Elasticsearch
    from langchain_elasticsearch import ElasticsearchStore
    cloud_id, api_key = os.getenv("ES_CLOUD_ID"), os.getenv("ES_API_KEY")
    if cloud_id and api_key:
        es = Elasticsearch(cloud_id=cloud_id, api_key=api_key)
    else:
        es = Elasticsearch(
            hosts=[os.environ["ES_HOST"]],
            basic_auth=(os.environ["ES_USERNAME"], os.environ["ES_PASSWORD"]),
        )
    ElasticsearchStore.from_documents(
        chunks, embedding=embeddings, es_client=es,
        index_name=os.environ["ES_INDEX"],
    )
    print(f"Indexed into Elasticsearch index {os.environ['ES_INDEX']}")
