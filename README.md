# 📄 Company Policy Assistant - RAG (Retrieval-Augmented Generation) Chatbot

A Retrieval-Augmented Generation (RAG) application that allows users to upload a company policy PDF and ask questions in natural language. The chatbot retrieves the most relevant information from the uploaded document using semantic search and generates accurate responses using the Mistral Large Language Model (LLM).

---

## 🚀 Problem Statement

Employees often spend a significant amount of time searching through lengthy company policy documents to find information about:

- Leave policies
- Notice period
- Work From Home (WFH) policy
- Attendance rules
- Holidays
- Reimbursement policy
- HR guidelines

Instead of manually searching through hundreds of pages, this application enables employees to ask questions in plain English and receive instant, context-aware answers.

---

## 💡 Solution

This project uses the **Retrieval-Augmented Generation (RAG)** architecture.

The workflow is:

1. User uploads a Company Policy PDF.
2. The PDF is split into smaller chunks.
3. Text chunks are converted into vector embeddings.
4. Embeddings are stored inside ChromaDB.
5. User asks a question.
6. The retriever fetches the most relevant chunks.
7. Mistral LLM generates an answer using only the retrieved context.

This significantly reduces hallucinations compared to a normal chatbot.

---

# 🏗️ Architecture

```
                Upload PDF
                     │
                     ▼
             PyPDFLoader
                     │
                     ▼
     RecursiveCharacterTextSplitter
                     │
                     ▼
           HuggingFace Embeddings
                     │
                     ▼
                ChromaDB
                     │
                     ▼
              Similarity Search
                     │
                     ▼
               Prompt Template
                     │
                     ▼
               Mistral LLM
                     │
                     ▼
             Generated Response
```

---

# ✨ Features

- Upload Company Policy PDF
- Semantic Search using ChromaDB
- Retrieval-Augmented Generation (RAG)
- Mistral LLM Integration
- LangChain Runnable API
- Context-aware Question Answering
- Modern Streamlit UI
- PDF Processing
- Automatic Text Chunking
- Vector Embeddings
- Fast Similarity Search

---

# 🛠️ Tech Stack

- Python
- LangChain
- Mistral AI
- ChromaDB
- HuggingFace Embeddings
- PyPDF
- Streamlit
- Python Dotenv

---

# 📂 Project Structure

```
Company-Policy-RAG/
│
├── app.py
├── config.py
├── rag.py
├── ingest.py
├── requirements.txt
├── .env
├── chroma_db/
└── data/
      └── company_policy.pdf
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/yourusername/company-policy-rag.git
```

Move into the project

```bash
cd company-policy-rag
```

Create virtual environment

```bash
python -m venv .venv
```

Activate virtual environment

### Windows

```bash
.venv\Scripts\activate
```

### Linux / Mac

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file

```env
MISTRAL_API_KEY=YOUR_API_KEY
```

---

# ▶️ Run the Project

```bash
streamlit run app.py
```

---

# 💬 Example Questions

- How many paid leaves are available?
- What is the notice period?
- Can employees work from home?
- What is the maternity leave policy?
- How many sick leaves are provided?
- What is the reimbursement policy?

---

# 📖 RAG Workflow

```
User Question
      │
      ▼
Retriever
      │
      ▼
Relevant Chunks
      │
      ▼
Prompt Template
      │
      ▼
Mistral LLM
      │
      ▼
Final Answer
```

---

# 📦 Dependencies

- langchain
- langchain-core
- langchain-community
- langchain-chroma
- langchain-huggingface
- langchain-mistralai
- chromadb
- sentence-transformers
- pypdf
- python-dotenv
- streamlit

---

# 📚 Learning Outcomes

This project demonstrates:

- Retrieval-Augmented Generation (RAG)
- Vector Databases
- Semantic Search
- Embedding Models
- Prompt Engineering
- LangChain Runnable API
- ChromaDB
- LLM Integration
- Streamlit Application Development

---

## ⭐ If you found this project useful, consider giving it a Star.
