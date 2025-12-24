# db-query-langchain
# 💬 Chat with SQL Database using LangChain & Groq

This project is a **Streamlit-based AI application** that allows users to **chat with a SQL database in natural language**.

It supports:
- 📁 **Local SQLite database**
- 🌐 **Remote MySQL database**

Using **LangChain SQL Agents**, the app converts natural language questions into SQL queries and returns results conversationally.

---

## 🚀 Features

- ✅ Chat with **SQLite** or **MySQL** databases
- ✅ Natural language → SQL query conversion
- ✅ Uses **LangChain SQL Agent**
- ✅ Powered by **Groq LLM**
- ✅ Interactive **Streamlit chat UI**
- ✅ Query reasoning visible (ReAct agent)

---

## 🧠 Tech Stack

- **Python**
- **Streamlit** – UI framework
- **LangChain** – SQL agent & toolkit
- **Groq LLM** – Fast inference
- **SQLite3 / MySQL**
- **SQLAlchemy**

---

## 📂 Project Structure

```text
├── app.py               # Streamlit application
├── student.db           # Local SQLite database (example)
├── requirements.txt     # Dependencies
├── README.md            # Documentation
