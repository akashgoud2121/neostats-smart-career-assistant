import os
import sys
from langchain_community.embeddings import FastEmbedEmbeddings

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))


def get_embedding_model():
    """Initialize and return the embedding model."""
    try:
        embedding_model = FastEmbedEmbeddings(
            model_name="BAAI/bge-small-en-v1.5"
        )
        return embedding_model
    except Exception as e:
        raise RuntimeError(f"Failed to initialize embedding model: {str(e)}")