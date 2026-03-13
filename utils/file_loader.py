import os
from langchain_community.document_loaders import PyPDFLoader, TextLoader


def load_documents_from_folder(folder_path):
    """Load PDF and TXT documents from a folder."""
    try:
        documents = []

        if not os.path.exists(folder_path):
            return documents

        for file_name in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file_name)

            try:
                if file_name.lower().endswith(".pdf"):
                    loader = PyPDFLoader(file_path)
                    documents.extend(loader.load())

                elif file_name.lower().endswith(".txt"):
                    loader = TextLoader(file_path, encoding="utf-8")
                    documents.extend(loader.load())

            except Exception as file_error:
                print(f"Error loading {file_name}: {str(file_error)}")

        return documents

    except Exception as e:
        raise RuntimeError(f"Failed to load documents: {str(e)}")