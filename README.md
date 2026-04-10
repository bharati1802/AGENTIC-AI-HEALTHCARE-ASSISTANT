# 🏥 Agentic Healthcare AI Assistant

## 🚀 Overview

This project is an **Agentic AI system** that simulates a Healthcare Claims Assistant. It uses a **Planner-Executor architecture** with Google Gemini LLM to automate decision-making and tool execution.

---

## 🧠 Features

* 🔹 Agentic AI (Planner + Executor)
* 🔹 JSON-based decision making
* 🔹 Healthcare query handling
* 🔹 Claim status checking (mock API)
* 🔹 Data storage using JSON
* 🔹 Streamlit web interface

---

## ⚙️ Tech Stack

* Python
* Streamlit
* Google Gemini (LLM)
* JSON (data storage)
* dotenv

---

## 📁 Project Structure

```
healthcare-ai-agent/
│
├── src/
│   ├── agents/
│   │   ├── planner.py
│   │   ├── executor.py
│   │
│   ├── tools/
│   │   ├── claims_api.py
│
├── app.py
├── data.json
├── .env
├── requirements.txt
```

---

## 🔧 Setup Instructions

### 1. Clone repository

```
git clone https://github.com/your-username/healthcare-ai-agent.git
cd healthcare-ai-agent
```

### 2. Create virtual environment

```
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Add API Key

Create `.env` file:

```
GEMINI_API_KEY=your_api_key_here
```

### 5. Run the app

```
streamlit run app.py
```

---

## 💬 Example Queries

* Check claim status Rahul
* My claim got rejected what should I do?
* How to file insurance claim?

---

## 🧠 Architecture

```
User → Planner Agent → JSON → Executor → Tool/API → Response
```

---

## 🎯 Future Improvements

* WhatsApp integration (Twilio)
* Database (SQLite / MongoDB)
* RAG (Retrieval-Augmented Generation)
* Multi-agent workflows

---

## 📌 Author

Bharati Patil

---


