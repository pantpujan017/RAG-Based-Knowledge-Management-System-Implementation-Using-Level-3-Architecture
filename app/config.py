# config.py
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Azure Storage
    AZURE_STORAGE_ACCOUNT = os.getenv('AZURE_STORAGE_ACCOUNT')
    AZURE_STORAGE_CONTAINER = os.getenv('AZURE_STORAGE_CONTAINER', 'knowledge-base')
    
    # Google Gemini
    GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
    GEMINI_MODEL = os.getenv('GEMINI_MODEL', 'gemini-1.5-pro')
    
    # Vector DB (unchanged - you're keeping ChromaDB)
    VECTOR_DB_PATH = 'vector_db'