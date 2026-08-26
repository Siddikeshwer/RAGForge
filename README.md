RAGForge

A Hybrid RAG application for asking questions across your documents.

RAGForge combines vector search + BM25 keyword search + reranking + LLM generation to produce grounded answers with source information.

✨ Features

📄 PDF, DOCX and TXT document support

🧩 Section-aware document chunking

🔢 Sentence Transformer embeddings

🗄️ ChromaDB vector search

🔎 BM25 keyword retrieval

🔀 Reciprocal Rank Fusion (RRF)

🎯 Cross-encoder reranking

🤖 Ox Alpha through OpenRouter

📚 Source-aware answers with page metadata

⚡ FastAPI backend

⚛️ React + Vite frontend

🌙 Dark developer-focused UI

🏗️ Architecture

                 Document
                    │
                    ▼
              Document Loader
                    │
                    ▼
               Chunker
                    │
          ┌─────────┴─────────┐
          ▼                   ▼
     Embeddings             BM25
          │                   │
          ▼                   ▼
      ChromaDB          Keyword Search
          │                   │
          └─────────┬─────────┘
                    ▼
             Hybrid Retrieval
                    │
                    ▼
                  RRF
                    │
                    ▼
              Cross-Encoder
               Reranking
                    │
                    ▼
                Ox Alpha
                    │
                    ▼
            Answer + Sources

🛠️ Tech Stack

Backend

Python

FastAPI

ChromaDB

Sentence Transformers

Rank-BM25

Cross-Encoder

OpenRouter

Frontend

React

Vite

Axios

📁 Project Structure

RAGForge/
├── backend/
│   ├── app/
│   │   ├── api/
│   │   └── rag/
│   ├── uploads/
│   ├── .env
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   ├── package.json
│   └── vite.config.js
│
├── .gitignore
└── README.md

🚀 Run Locally

1. Clone

git clone https://github.com/YOUR_USERNAME/RAGForge.git
cd RAGForge

2. Backend

cd backend
py -m pip install -r requirements.txt

Create backend/.env:

OPENROUTER_API_KEY=your_openrouter_api_key
MODEL=stealth/ox-alpha

Start FastAPI:

py -m uvicorn app.main:app --reload

Backend:

http://127.0.0.1:8000

API docs:

http://127.0.0.1:8000/docs

3. Frontend

Open another terminal:

cd frontend
npm install
npm run dev

Open:

http://localhost:5173

📚 Supported Documents

Format

Support

PDF

✅

DOCX

✅

TXT

✅

Scanned PDF

⚠️ OCR not included

🔍 How Hybrid RAG Works

RAGForge uses two retrieval strategies:

Vector Search

Finds documents based on semantic meaning using embeddings.

BM25

Finds documents based on keyword relevance.

The results are combined using Reciprocal Rank Fusion (RRF) and then passed through a cross-encoder reranker before generation.

This helps balance semantic similarity with exact keyword matching.

🤖 Generation

The final context is sent to Ox Alpha through OpenRouter.

The model is instructed to:

Answer only from retrieved context

Avoid inventing information

Cite relevant sources

Say when the answer cannot be found

🔐 Environment Variables

Never commit your API key.

OPENROUTER_API_KEY=your_key
MODEL=stealth/ox-alpha

.env is included in .gitignore.

⚠️ Current Limitations

Scanned/image-only PDFs require OCR

Document management is currently basic

Free LLM endpoints may be rate-limited

No authentication system yet

🎯 Roadmap

Multi-document management

Document-specific querying

PDF viewer with clickable page citations

OCR support

Chat history

Streaming responses

LLM fallback model

Improved document management

Production deployment

📸 Demo

Upload a document → index it → ask a question → RAGForge retrieves the relevant passages and generates a grounded answer with sources.

📜 License

MIT License
