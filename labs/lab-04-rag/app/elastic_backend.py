"""Elasticsearch / watsonx Discovery retriever — production backend.

Supports two auth modes:
  - IBM Cloud Databases for Elasticsearch:   ES_CLOUD_ID + ES_API_KEY
  - Self-managed Elasticsearch:              ES_HOST + ES_USERNAME + ES_PASSWORD
"""
import os
from dotenv import load_dotenv
from elasticsearch import Elasticsearch
from langchain_elasticsearch import ElasticsearchStore
from langchain_huggingface import HuggingFaceEmbeddings

load_dotenv()
if os.path.exists("es.env"):
    load_dotenv("es.env")


def build_elastic_retriever():
    cloud_id = os.getenv("ES_CLOUD_ID")
    api_key  = os.getenv("ES_API_KEY")
    host     = os.getenv("ES_HOST")
    user     = os.getenv("ES_USERNAME")
    pwd      = os.getenv("ES_PASSWORD")

    if cloud_id and api_key:
        es = Elasticsearch(cloud_id=cloud_id, api_key=api_key)
    else:
        es = Elasticsearch(hosts=[host], basic_auth=(user, pwd))

    index_name  = os.environ["ES_INDEX"]
    embed_model = os.getenv("EMBEDDINGS_MODEL",
                            "sentence-transformers/all-MiniLM-L6-v2")
    embeddings = HuggingFaceEmbeddings(model_name=embed_model)

    store = ElasticsearchStore(
        es_url=None,
        index_name=index_name,
        embedding=embeddings,
        es_client=es,
    )
    return store.as_retriever(search_kwargs={"k": 4})
