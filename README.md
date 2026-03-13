# NeoStats Smart Career Assistant

NeoStats Smart Career Assistant is a Streamlit-based AI chatbot built for the NeoStats AI Engineer assignment. It helps students and job seekers with interview preparation, resume improvement, job search guidance, and career-related questions.

The chatbot supports:
- Retrieval-Augmented Generation (RAG) using local documents
- Live web search for recent information
- Concise and Detailed response modes
- Groq-powered conversational responses
- Source visibility for retrieved documents and web context
- User document upload for personalized retrieval

---

## Use Case Objective

The goal of this project is to build an intelligent chatbot that does more than answer generic questions. This chatbot is designed as a **Smart Career Assistant** that can:
- answer career and interview questions
- retrieve information from local documents
- use live web search when recent information is helpful
- adjust the response style based on user preference
- support uploaded user documents for personalized guidance

This makes the chatbot practical for real-world use in interview preparation and career guidance.

---

## Features Implemented

### 1. RAG Integration
- Loads local `.txt` and `.pdf` files from `data/docs/`
- Supports user-uploaded `.txt` and `.pdf` documents
- Splits documents into chunks
- Generates embeddings for document chunks
- Stores them in a FAISS vector store
- Retrieves relevant context for user questions

### 2. Live Web Search Integration
- Performs real-time web search for recent and relevant information
- Adds web context to the response generation process
- Displays the search context in the UI for transparency

### 3. Response Modes
- **Concise Mode**: short and summarized answers
- **Detailed Mode**: more structured and expanded answers

### 4. Modular Architecture
The code is organized into:
- `config/` for environment-based settings
- `models/` for LLM and embedding logic
- `utils/` for file loading, RAG, prompts, and web search
- `app.py` for the Streamlit interface

### 5. Source Display
- Shows document sources used in RAG
- Shows web search context used for responses

### 6. Upload Support
- Allows users to upload their own TXT and PDF files
- Uses uploaded documents for personalized question answering

---

## Project Structure

```bash
project/
├── config/
│   └── config.py
│
├── data/
│   └── docs/
│       ├── interview_guide.txt
│       ├── resume_tips.txt
│       ├── sql_interview_tips.txt
│       ├── behavioral_interview_tips.txt
│       └── job_search_strategy.txt
│
├── models/
│   ├── llm.py
│   └── embeddings.py
│
├── utils/
│   ├── file_loader.py
│   ├── prompt_utils.py
│   ├── rag_utils.py
│   └── web_search.py
│
├── uploaded_docs/
├── app.py
├── requirements.txt
├── .env.example
└── README.md
```

Tech Stack

Frontend / UI: Streamlit

LLM: Groq via LangChain

Embeddings: FastEmbed

Vector Store: FAISS

Document Loading: LangChain community loaders

Web Search: DDGS

Environment Management: python-dotenv



Setup Instructions
1. Clone the repository
```
git clone https://github.com/YOUR_USERNAME/neostats-smart-career-assistant.git
cd neostats-smart-career-assistant
```
2. Create and activate a virtual environment
```
Windows PowerShell
python -m venv .venv
.venv\Scripts\Activate.ps1
```
macOS / Linux
```
python -m venv .venv
source .venv/bin/activate
```
3. Install dependencies
```
pip install -r requirements.txt
```
4. Create a .env file

Create a .env file in the project root using the values from .env.example.

Example:
```
GROQ_API_KEY=your_groq_api_key_here
DEFAULT_CHAT_MODEL=llama-3.1-8b-instant
APP_TITLE=NeoStats Smart Career Assistant
DOCS_PATH=data/docs
CHUNK_SIZE=500
CHUNK_OVERLAP=100
TOP_K_RESULTS=3
Run the App Locally
streamlit run app.py
```

How It Works
```
The user enters a career-related question in the Streamlit chat UI.

The app optionally retrieves relevant context from local documents using FAISS.

The app optionally performs a live web search for recent information.

A system prompt is built using:

selected response mode

retrieved document context

web search context

Groq generates the final answer.

The UI displays:

the chatbot response

document sources used

live web search context

If the user uploads documents, the app uses those uploaded files as the active knowledge source for retrieval.
```

Example Questions

Detailed Mode
```
Create a 7-day preparation plan for a data analytics interview using the uploaded documents and recent web information.
```
What interview roles should I prepare for based on my uploaded resume and recent web information?

Concise Mode
```
Give me concise resume tips for a junior data analyst role based on the uploaded documents.

Give me concise resume improvement tips based on my uploaded document.
```

Streamlit Cloud Deployment

This project can be deployed on Streamlit Cloud.

Deployment Steps
```
Push the project to GitHub

Open Streamlit Cloud

Create a new app from the GitHub repository

Select app.py as the main file
```

Add secrets in Streamlit Cloud for:

```
GROQ_API_KEY

DEFAULT_CHAT_MODEL

APP_TITLE

DOCS_PATH

CHUNK_SIZE

CHUNK_OVERLAP

TOP_K_RESULTS

```

Example secrets:

```
GROQ_API_KEY = "your_groq_api_key"
DEFAULT_CHAT_MODEL = "llama-3.1-8b-instant"
APP_TITLE = "NeoStats Smart Career Assistant"
DOCS_PATH = "data/docs"
CHUNK_SIZE = "500"
CHUNK_OVERLAP = "100"
TOP_K_RESULTS = "3"
```
