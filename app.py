import streamlit as st
import os
import sys
from pathlib import Path
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from models.llm import get_chat_model
from utils.prompt_utils import build_system_prompt
from utils.rag_utils import build_vectorstore, retrieve_relevant_context
from utils.web_search import search_web
from config.config import APP_TITLE, DEFAULT_CHAT_MODEL, DOCS_PATH


UPLOAD_DIR = "uploaded_docs"


def save_uploaded_files(uploaded_files):
    """Save uploaded files locally for RAG processing."""
    try:
        os.makedirs(UPLOAD_DIR, exist_ok=True)

        saved_files = []
        for uploaded_file in uploaded_files:
            file_path = os.path.join(UPLOAD_DIR, uploaded_file.name)
            with open(file_path, "wb") as f:
                f.write(uploaded_file.getbuffer())
            saved_files.append(file_path)

        return saved_files

    except Exception as e:
        raise RuntimeError(f"Failed to save uploaded files: {str(e)}")


def get_chat_response(chat_model, messages, system_prompt, response_mode):
    """Get response from the chat model."""
    try:
        formatted_messages = [SystemMessage(content=system_prompt)]

        for i, msg in enumerate(messages):
            if msg["role"] == "user":
                content = msg["content"]

                if i == len(messages) - 1:
                    if response_mode == "Concise":
                        content = (
                            f"{content}\n\n"
                            "IMPORTANT: Follow the selected UI response mode strictly. "
                            "Return a concise answer only. "
                            "Maximum 5 short sentences and maximum 80 words total. "
                            "No headings. "
                            "No bullet points. "
                            "No long explanations. "
                            "Summarize only the most important points. "
                            "Even if the user asks for a detailed answer, keep it concise."
                        )
                    else:
                        content = (
                            f"{content}\n\n"
                            "IMPORTANT: Follow the selected UI response mode strictly. "
                            "Return a detailed, practical, and structured answer. "
                            "Use short headings where useful. "
                            "Give realistic steps and examples. "
                            "Avoid repetition."
                        )

                formatted_messages.append(HumanMessage(content=content))

            elif msg["role"] == "assistant":
                formatted_messages.append(AIMessage(content=msg["content"]))

        response = chat_model.invoke(formatted_messages)

        if hasattr(response, "content"):
            return response.content.strip()

        return str(response).strip()

    except Exception as e:
        return f"Error getting response: {str(e)}"


def instructions_page():
    st.title("The Chatbot Blueprint")
    st.markdown("Welcome! Follow these instructions to set up and use the chatbot.")

    st.markdown("""
    ## Installation

    ```bash
    pip install -r requirements.txt
    ```

    ## Environment Variables

    Create a `.env` file in the project root and add:

    ```env
    GROQ_API_KEY=your_groq_api_key
    DEFAULT_CHAT_MODEL=llama-3.1-8b-instant
    APP_TITLE=NeoStats Smart Career Assistant
    DOCS_PATH=data/docs
    CHUNK_SIZE=500
    CHUNK_OVERLAP=100
    TOP_K_RESULTS=3
    ```

    ## Features

    - Groq-based chatbot
    - RAG over local TXT/PDF documents
    - Upload your own documents
    - Live web search
    - Concise and Detailed response modes
    """)


@st.cache_resource(show_spinner=False)
def load_vectorstore_cached(folder_path):
    """Load and cache vectorstore based on folder path."""
    try:
        vectorstore, split_docs = build_vectorstore(folder_path)
        return vectorstore, split_docs
    except Exception as e:
        st.error(f"Error loading vector store: {str(e)}")
        return None, []


def chat_page(response_mode, enable_rag, enable_web_search, active_docs_path):
    st.title(f"🤖 {APP_TITLE}")
    st.caption(f"Current model: {DEFAULT_CHAT_MODEL}")
    st.caption(f"Response mode: {response_mode}")

    try:
        chat_model = get_chat_model()
    except Exception as e:
        st.error(str(e))
        st.stop()

    vectorstore = None
    split_docs = []

    if enable_rag:
        vectorstore, split_docs = load_vectorstore_cached(active_docs_path)
        st.caption(f"Document search enabled | Loaded chunks: {len(split_docs)} | Docs folder: {active_docs_path}")
    else:
        st.caption("Document search disabled")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

            if message["role"] == "assistant":
                if message.get("rag_sources"):
                    with st.expander("Document Sources Used"):
                        for source in message["rag_sources"]:
                            st.write(f"- {source}")

                if message.get("web_context"):
                    with st.expander("Live Web Search Context"):
                        st.write(message["web_context"])

    if prompt := st.chat_input("Type your message here..."):
        st.session_state.messages.append({
            "role": "user",
            "content": prompt
        })

        with st.chat_message("user"):
            st.markdown(prompt)

        rag_context = ""
        rag_sources = []
        web_context = ""

        if enable_rag and vectorstore is not None:
            rag_context, rag_sources = retrieve_relevant_context(vectorstore, prompt)

        if enable_web_search:
            web_context = search_web(prompt)

        short_web_context = web_context[:1500] if web_context else ""

        system_prompt = build_system_prompt(
            response_mode=response_mode,
            rag_context=rag_context,
            web_context=short_web_context
        )

        recent_messages = st.session_state.messages[-6:]

        with st.chat_message("assistant"):
            with st.spinner("Getting response..."):
                response = get_chat_response(
                    chat_model,
                    recent_messages,
                    system_prompt,
                    response_mode
                )
                st.markdown(response)

                if enable_rag and rag_sources:
                    with st.expander("Document Sources Used"):
                        for source in rag_sources:
                            st.write(f"- {source}")

                if enable_web_search and short_web_context:
                    with st.expander("Live Web Search Context"):
                        st.write(short_web_context)

        st.session_state.messages.append({
            "role": "assistant",
            "content": response,
            "rag_sources": rag_sources,
            "web_context": short_web_context
        })


def main():
    st.set_page_config(
        page_title="NeoStats ChatBot",
        page_icon="🤖",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    response_mode = "Concise"
    enable_rag = True
    enable_web_search = True
    active_docs_path = DOCS_PATH

    with st.sidebar:
        st.title("Navigation")
        page = st.radio("Go to:", ["Chat", "Instructions"], index=0)

        if page == "Chat":
            st.divider()

            response_mode = st.radio(
                "Response Mode",
                ["Concise", "Detailed"],
                index=0
            )

            enable_rag = st.checkbox("Enable Document Search (RAG)", value=True)
            enable_web_search = st.checkbox("Enable Live Web Search", value=True)

            st.divider()
            st.subheader("Upload Documents")
            uploaded_files = st.file_uploader(
                "Upload TXT or PDF files",
                type=["txt", "pdf"],
                accept_multiple_files=True
            )

            if uploaded_files:
                save_uploaded_files(uploaded_files)
                active_docs_path = UPLOAD_DIR
                st.success(f"{len(uploaded_files)} file(s) uploaded successfully.")
            else:
                active_docs_path = DOCS_PATH

            st.divider()
            if st.button("🗑️ Clear Chat History", use_container_width=True):
                st.session_state.messages = []
                st.rerun()

    if page == "Instructions":
        instructions_page()
    elif page == "Chat":
        chat_page(response_mode, enable_rag, enable_web_search, active_docs_path)


if __name__ == "__main__":
    main()