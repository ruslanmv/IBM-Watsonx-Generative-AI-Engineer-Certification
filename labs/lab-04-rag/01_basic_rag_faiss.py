"""
Lab 04 · step 1 — End-to-end RAG in one file (Slate + FAISS).

Good for prototypes and the exam scenario "prototype on a laptop with
IBM-native embeddings". For governed production, prefer Elasticsearch /
watsonx Discovery (see app/elastic_backend.py).

Run:
    python 01_basic_rag_faiss.py
"""
import glob
import os
from pathlib import Path
from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader, PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA
from langchain_ibm import WatsonxLLM, WatsonxEmbeddings

load_dotenv()
URL        = os.environ["WATSONX_URL"]
APIKEY     = os.environ["WATSONX_APIKEY"]
PROJECT_ID = os.environ["WATSONX_PROJECT_ID"]
LLM_ID     = os.getenv("LLM_MODEL_ID",   "ibm/granite-3-2-8b-instruct")
EMB_ID     = os.getenv("WATSONX_EMBEDDER", "ibm/slate-125m-english-rtrvr-v2")
DATA_DIR   = Path(os.getenv("DATA_DIR", "./data"))
DATA_DIR.mkdir(exist_ok=True)

# 1) Load — mix of .txt and .pdf supported out of the box
docs = []
for path in glob.glob(str(DATA_DIR / "*")):
    if path.endswith(".pdf"):
        docs.extend(PyPDFLoader(path).load())
    elif path.endswith((".txt", ".md")):
        docs.extend(TextLoader(path, encoding="utf-8").load())
if not docs:
    sample = DATA_DIR / "sample.txt"
    sample.write_text(
        "IBM watsonx Discovery is the managed hybrid retrieval service. It "
        "runs BM25 keyword search and dense-vector search over the same "
        "Elasticsearch index, then re-ranks the top results with a cross-encoder. "
        "It integrates with watsonx.governance for lineage and drift tracking."
    )
    docs.extend(TextLoader(str(sample), encoding="utf-8").load())
    print(f"No documents found — wrote a tiny sample at {sample}")

print(f"Loaded {len(docs)} document(s).")

# 2) Chunk
splitter = RecursiveCharacterTextSplitter(chunk_size=512, chunk_overlap=64)
chunks = splitter.split_documents(docs)
print(f"Produced {len(chunks)} chunk(s).")

# 3) Embed + index
emb = WatsonxEmbeddings(
    model_id=EMB_ID, url=URL, apikey=APIKEY, project_id=PROJECT_ID,
)
store = FAISS.from_documents(chunks, emb)

# 4) Generator + grounded prompt
llm = WatsonxLLM(
    model_id=LLM_ID, url=URL, apikey=APIKEY, project_id=PROJECT_ID,
    params={
        "decoding_method": "greedy",
        "max_new_tokens":  int(os.getenv("LLM_MAX_NEW_TOKENS", 300)),
        "temperature":     float(os.getenv("LLM_TEMPERATURE", 0.2)),
    },
)
qa = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=store.as_retriever(search_type="mmr",
                                 search_kwargs={"k": 4, "fetch_k": 20}),
    return_source_documents=True,
)

# 5) Ask
question = "What does watsonx Discovery use under the hood?"
result = qa.invoke({"query": question})
print("\nANSWER:\n", result["result"].strip())
print("\nSOURCES:")
for i, doc in enumerate(result["source_documents"], 1):
    print(f"  [{i}] {doc.metadata}  {doc.page_content[:120]!r} ...")
