import chromadb
from langchain.vectorstores import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings  # ← NEW
import os

class VectorStore:
    def __init__(self, path):
        self.embeddings = GoogleGenerativeAIEmbeddings(           # ← NEW
            model="models/embedding-001",                         # ← NEW
            google_api_key=os.getenv("GEMINI_API_KEY")            # ← NEW
        )
        self.vector_store = Chroma(
            persist_directory=path,
            embedding_function=self.embeddings
        )

    def add_documents(self, documents):
        self.vector_store.add_documents(documents)
        
    def similarity_search(self, query, k=4):
        return self.vector_store.similarity_search(query, k=k)
    
    def as_retriever(self):                    # ← ADD this for GeminiService
        return self.vector_store.as_retriever()