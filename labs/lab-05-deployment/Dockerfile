# Image for the lab-04 RAG application (server.py + app/).
#
# Build from the lab-04 directory so the build context contains app/, server.py,
# rag_cli.py and requirements.txt:
#
#   cd labs/lab-04-rag
#   docker build -f ../lab-05-deployment/Dockerfile -t cert-rag:dev .
#   docker run --rm -p 8001:8001 --env-file .env cert-rag:dev

FROM python:3.11-slim

WORKDIR /app

# System deps for faiss / sentence-transformers wheels
RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential libgomp1 \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app
ENV PYTHONPATH=/app
EXPOSE 8001
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8001"]
