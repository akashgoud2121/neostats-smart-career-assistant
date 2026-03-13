import os
from dotenv import load_dotenv

try:
    load_dotenv()

    GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")
    DEFAULT_CHAT_MODEL = os.getenv("DEFAULT_CHAT_MODEL", "llama-3.1-8b-instant")
    APP_TITLE = os.getenv("APP_TITLE", "NeoStats Smart Career Assistant")

    CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", 500))
    CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP", 100))
    TOP_K_RESULTS = int(os.getenv("TOP_K_RESULTS", 3))
    DOCS_PATH = os.getenv("DOCS_PATH", "data/docs")

except Exception as e:
    raise RuntimeError(f"Failed to load configuration: {str(e)}")