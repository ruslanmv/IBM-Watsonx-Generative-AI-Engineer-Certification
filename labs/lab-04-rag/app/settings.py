"""Centralised settings for the lab-04 RAG app.

Loaded from .env via pydantic-settings. Same keys as the watsonx-workshop
rag-app, so you can swap them.
"""
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    WATSONX_URL: str | None = None
    WATSONX_APIKEY: str | None = None
    WATSONX_PROJECT_ID: str | None = None
    LLM_MODEL_ID: str = "ibm/granite-3-2-8b-instruct"
    LLM_TEMPERATURE: float = 0.2
    LLM_MAX_NEW_TOKENS: int = 300
    RAG_BACKEND: str = "chroma"     # 'chroma' or 'elastic'
    CHROMA_DIR: str = ".chroma"
    EMBEDDINGS_MODEL: str = "sentence-transformers/all-MiniLM-L6-v2"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
