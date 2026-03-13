import os
import sys
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from config.config import CHUNK_SIZE, CHUNK_OVERLAP, TOP_K_RESULTS, DOCS_PATH
from models.embeddings import get_embedding_model
from utils.file_loader import load_documents_from_folder


def build_vectorstore():
    """Load documents, split them, and build a FAISS vector store."""
    try:
        documents = load_documents_from_folder(DOCS_PATH)

        if not documents:
            return None, []

        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=CHUNK_SIZE,
            chunk_overlap=CHUNK_OVERLAP
        )

        split_docs = text_splitter.split_documents(documents)

        embedding_model = get_embedding_model()
        vectorstore = FAISS.from_documents(split_docs, embedding_model)

        return vectorstore, split_docs

    except Exception as e:
        raise RuntimeError(f"Failed to build vector store: {str(e)}")


def retrieve_relevant_context(vectorstore, query, top_k=TOP_K_RESULTS):
    """Retrieve relevant chunks for a user query."""
    try:
        if vectorstore is None:
            return "", []

        results = vectorstore.similarity_search(query, k=top_k)

        if not results:
            return "", []

        context_parts = []
        sources = []

        for doc in results:
            context_parts.append(doc.page_content.strip())

            source_name = doc.metadata.get("source", "Unknown source")
            if source_name not in sources:
                sources.append(source_name)

        context_text = "\n\n".join(context_parts)
        return context_text, sources

    except Exception as e:
        raise RuntimeError(f"Failed to retrieve relevant context: {str(e)}")