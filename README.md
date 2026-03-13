# NeoStats Smart Career Assistant

NeoStats Smart Career Assistant is a Streamlit-based AI chatbot built for the NeoStats AI Engineer assignment.  
It helps students and job seekers with interview preparation, resume improvement, job search guidance, and career-related questions.

The chatbot supports:
- Retrieval-Augmented Generation (RAG) using local documents
- Live web search for recent information
- Concise and Detailed response modes
- Groq-powered conversational responses
- Source visibility for retrieved documents and web context

---

## Use Case Objective

The goal of this project is to build an intelligent chatbot that does more than answer generic questions.  
This chatbot is designed as a **Smart Career Assistant** that can:
- answer career and interview questions
- retrieve information from local documents
- use live web search when recent information is helpful
- adjust the response style based on user preference

This makes the chatbot practical for real-world use in interview preparation and career guidance.

---

## Features Implemented

### 1. RAG Integration
- Loads local `.txt` and `.pdf` files from `data/docs/`
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
macOS / Linux
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
```
5. Run the App Locally
```
streamlit run app.py
```

How It Works

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

Example Questions
Detailed Mode

Create a 7-day preparation plan for a data analytics interview using the uploaded documents and recent web information.

Concise Mode

Give me concise resume tips for a junior data analyst role based on the uploaded documents.

Streamlit Cloud Deployment

This project can be deployed on Streamlit Cloud.

Deployment steps

Push the project to GitHub

Open Streamlit Cloud

Create a new app from the GitHub repository

Select app.py as the main file

Add secrets in Streamlit Cloud for:

GROQ_API_KEY

DEFAULT_CHAT_MODEL

APP_TITLE

DOCS_PATH

CHUNK_SIZE

CHUNK_OVERLAP

TOP_K_RESULTS

Environment Variables
Variable	Description
GROQ_API_KEY	Groq API key
DEFAULT_CHAT_MODEL	Groq model name
APP_TITLE	Chatbot title shown in UI
DOCS_PATH	Path to knowledge base documents
CHUNK_SIZE	Chunk size for splitting documents
CHUNK_OVERLAP	Chunk overlap for retrieval
TOP_K_RESULTS	Number of retrieved chunks
Challenges Faced

Dependency issues with sentence-transformers, torch, and torchvision

Fixing package compatibility problems

Improving concise vs detailed response control

Preserving source/context display across Streamlit reruns

Final Outcome

The final chatbot successfully demonstrates:

modular chatbot architecture

local document-based retrieval

real-time web search

response-mode switching

deployment-ready Streamlit application

Notes

API keys are not committed to the repository

Use .env locally and Streamlit secrets for deployment

The sample knowledge base can be extended with more career-related documents

Author

Akash
NeoStats AI Engineer Assignment Submission


```md
## Live Demo
Streamlit App: 