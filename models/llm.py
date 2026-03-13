import os
import sys
from langchain_groq import ChatGroq

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from config.config import GROQ_API_KEY, DEFAULT_CHAT_MODEL


def get_chat_model(model_name=None, temperature=0.2):
    try:
        if not GROQ_API_KEY:
            raise ValueError("GROQ_API_KEY is missing.")

        selected_model = model_name or DEFAULT_CHAT_MODEL

        return ChatGroq(
            api_key=GROQ_API_KEY,
            model=selected_model,
            temperature=temperature,
        )
    except Exception as e:
        raise RuntimeError(f"Failed to initialize Groq model: {str(e)}")