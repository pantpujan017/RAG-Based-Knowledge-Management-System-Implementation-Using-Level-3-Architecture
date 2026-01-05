```markdown
# RAG-Based Knowledge-Management System (Level-3 Architecture)

A lightweight **Retrieval-Augmented-Generation** service built with Flask, ChromaDB, Google Gemini and Azure Blob Storage.  
Upload PDF/TXT files via the web UI and ask questions—answers are generated from your own documents.

## Features
* Drag-and-drop document upload (PDF / TXT)  
* Automatic text chunking & vector embedding (Gemini embeddings)  
* Persistent storage in Azure Blob + Chroma vector DB inside the container  
* Question-answering powered by Gemini Pro  
* Full CI/CD: GitHub Actions → Azure Container Registry → Ubuntu VM

## Local Development
```bash
# 1. create env
conda create -n ragapp python=3.11 -y
conda activate ragapp

# 2. install deps
pip install -r requirements.txt

# 3. add env vars (optional if you use Azure in prod only)
export GEMINI_API_KEY=your_key
export AZURE_STORAGE_ACCOUNT=your_account
export AZURE_STORAGE_CONTAINER=your_container

# 4. run
python app/main.py
# open http://localhost:8080
```

## Tech Stack
* **Backend**: Flask, LangChain, Google Gemini, ChromaDB  
* **Storage**: Azure Blob Storage  
* **Infra**: Docker, Azure Container Registry, Azure VM (self-hosted runner)  
* **CI/CD**: GitHub Actions OIDC


## CI/CD Pipeline
`.github/workflows/azure-cicd.yml`  
1. lint + unit tests  
2. build & push Docker image to ACR  
3. pull image on VM, stop old container, start new one on :8080

## Repo Structure
```
├── app/
│   ├── main.py              # Flask server
│   ├── models/
│   └── services/
├── requirements.txt
├── Dockerfile
└── .github/workflows/
    └── azure-cicd.yml
```

