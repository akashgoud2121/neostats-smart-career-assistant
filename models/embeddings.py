import os
import sys
from fastembed import TextEmbedding

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))


class FastEmbedWrapper:
    def __init__(self, model_name="BAAI/bge-small-en-v1.5"):
        self.model = TextEmbedding(model_name=model_name)

    def embed_documents(self, texts):
        embeddings = list(self.model.embed(texts))
        return [embedding.tolist() for embedding in embeddings]

    def embed_query(self, text):
        embedding = next(self.model.embed([text]))
        return embedding.tolist()

    def __call__(self, text):
        return self.embed_query(text)


def get_embedding_model():
    """Initialize and return the embedding model."""
    try:
        embedding_model = FastEmbedWrapper(
            model_name="BAAI/bge-small-en-v1.5"
        )
        return embedding_model
    except Exception as e:
        raise RuntimeError(f"Failed to initialize embedding model: {str(e)}")