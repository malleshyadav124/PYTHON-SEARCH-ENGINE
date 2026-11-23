# 🐍 Python Search Engine

A Python-focused AI search engine that accepts Python-related programming queries and generates concise, structured answers using a locally running Large Language Model (LLM).

The application is built using **Flask** for the web interface and backend, **Ollama** for local AI inference, and **Llama 3.2** for generating answers. Markdown responses are rendered into structured HTML using **marked.js**.

---

## 📌 Features

- 🔍 Python-focused search
- 🤖 AI-powered answers using a locally running LLM
- 🐍 Python-specific query filtering
- ⚖️ Comparisons between Python and other programming languages
- 📊 Structured comparison tables
- 📝 Markdown-formatted responses
- 💻 Python code examples
- ⚡ Local AI processing using Ollama
- 🎨 Clean and responsive web interface
- ⏳ Search/loading indicator
- 🔒 No external AI API key required

---

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Application logic |
| Flask | Web framework |
| Ollama | Local LLM runtime |
| Llama 3.2 | AI response generation |
| HTML | Web page structure |
| CSS | User interface styling |
| JavaScript | Frontend functionality |
| marked.js | Markdown rendering |

---

## 🏗️ System Architecture

```text
User
  │
  ▼
Web Interface
  │
  ▼
Flask Application
  │
  ▼
Python Query Validation
  │
  ▼
Query Enhancement
  │
  ▼
Prompt Generation
  │
  ▼
Ollama
  │
  ▼
Llama 3.2
  │
  ▼
Markdown Response
  │
  ▼
marked.js
  │
  ▼
HTML + CSS
  │
  ▼
Structured Answer
```

---

## ⚙️ How It Works

### 1. User enters a query

The user enters a Python-related question through the search interface.

Example:

```text
What is a Python dictionary?
```

### 2. Query validation

The Flask application checks whether the query is related to Python.

Python-related questions are accepted, while clearly unrelated topics are rejected.

### 3. Query enhancement

If required, the application adds Python context to the query before sending it to the AI model.

For example:

```text
What is a list?
```

can be interpreted in the context of Python.

### 4. Prompt generation

The application creates a structured prompt that instructs the AI to provide:

- Clear explanations
- Similarities and differences for comparison questions
- Tables where appropriate
- Python examples
- A short conclusion

### 5. Local AI processing

The query is sent to **Ollama**, which runs the Llama 3.2 model locally.

### 6. Markdown rendering

The AI generates Markdown-formatted content.

The frontend uses `marked.js` to convert the Markdown into HTML.

This allows the application to display:

- Headings
- Bullet points
- Tables
- Bold text
- Code blocks
- Structured sections

---

## 💡 Example Queries

### Basic Python Query

```text
What is a Python list?
```

### Concept Query

```text
Explain Python functions
```

### Comparison Query

```text
Compare Python and Java
```

### Another Comparison

```text
Python vs C++
```

### JavaScript Comparison

```text
Difference between Python and JavaScript
```

---

## 📊 Example Comparison Output

For a query such as:

```text
Compare Python and Java
```

the system generates a structured response containing:

```text
🐍 Python vs Java

Overview

🔹 Similarities

🔹 Key Differences

| Feature | Python | Java |
|---------|--------|------|
| Syntax | Simple | More verbose |
| Typing | Dynamic | Static |
| Performance | Generally slower | Generally faster |

🐍 Python Perspective

💡 Simple Example

✅ In Short
```

---

## 📁 Project Structure

```text
python-search-engine/
│
├── app.py
│
├── templates/
│   └── index.html
│
├── .gitignore
│
└── README.md
```

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone <your-repository-url>
```

Move into the project directory:

```bash
cd python-search-engine
```

### 2. Install Flask

```bash
pip install flask requests
```

### 3. Install Ollama

Install Ollama on your system and make sure it is running.

### 4. Download the Llama model

```bash
ollama pull llama3.2:3b
```

### 5. Run the application

```bash
python app.py
```

### 6. Open the application

Open your browser and visit:

```text
http://127.0.0.1:5000
```

---

## 🔄 Response Processing

The application follows this process:

```text
User Query
     ↓
Query Validation
     ↓
Query Enhancement
     ↓
AI Prompt
     ↓
Ollama + Llama 3.2
     ↓
Markdown Response
     ↓
marked.js
     ↓
HTML Rendering
     ↓
Structured Output
```

---

## 🔐 Privacy

The AI model runs locally through Ollama. User queries are processed by the local Llama model rather than being sent to an external AI API.

---

## 🔮 Future Enhancements

Possible future improvements include:

- 🔎 Search history
- 📚 Python documentation integration
- 🔗 Web-based Python documentation search
- 🧠 More advanced query classification
- 💬 Conversation history
- 🌙 Dark/light mode
- 📋 Copy-code functionality
- 🐍 Python code execution
- 🔊 Voice-based search
- 📱 Improved mobile interface
- 🔍 Semantic search using embeddings
- 📖 Integration with Python documentation and tutorials

---

## 🎯 Project Objective

The objective of this project is to develop a focused AI-powered search system that helps users understand Python programming concepts through concise, structured, and easy-to-understand responses.

---

## 👨‍💻 Author

Developed as an academic/personal project for exploring:

- Python
- Flask
- Local LLMs
- Ollama
- Prompt Engineering
- AI-powered Search
- Markdown Rendering