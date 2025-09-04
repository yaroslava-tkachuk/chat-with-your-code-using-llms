# Chat with Your Code using LlamaIndex + ActiveLoop Deep Lake

This project allows you to **chat with your GitHub code** using **LlamaIndex** and **ActiveLoop Deep Lake**.  
It implements **RAG (Retrieval-Augmented Generation)** to index your codebase and provide AI-powered code search and Q&A.

---

## 🚀 Features
- Index an entire GitHub repository
- Store embeddings in **ActiveLoop Deep Lake**
- Query your codebase with **LlamaIndex**
- Simple command-line interface for interaction

---

## 🛠 Installation & Setup

### 1. **Clone the repository**
```bash
git clone <your-repo-url>
cd <your-repo-folder>
```

### 2. Create and activate virtual environment
```bash
python3 -m venv .venv
```

### 3. Activate the venv:
#### Mac/Linux:
```bash
source .venv/bin/activate
```
#### Windows (PowerShell):
```bash
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

#### 4. Set your environment variables in  .env file in the root of the repo.

### 5. Run the App
```bash
python -m app.main
```
