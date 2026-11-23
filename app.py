from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# 🔹 Check Python-related query
def is_python_query(query):
    query_lower = query.lower()

    # Clearly unrelated topics
    blocked_words = [
        "cricket",
        "football",
        "politics",
        "movies",
        "weather",
        "recipe",
        "songs"
    ]

    if any(word in query_lower for word in blocked_words):
        return False

    # Python must be involved
    if "python" in query_lower:
        return True

    return False
def enhance_query(query):
    if "python" not in query.lower():
        return query + " in python"
    return query
def get_answer(query):
    try:
        prompt = f"""
You are a Python-focused programming assistant.

Your job is to answer programming questions with Python as the main focus.

RULES:
- Answer Python-related questions.
- Comparisons between Python and other programming languages are allowed.
- For comparisons, always explain Python first and then compare it with the other language.
- Do not answer completely unrelated questions.
- Keep answers clear and student-friendly.
- Do not repeat information.
- Do not leave the answer incomplete.
- Do not invent technical facts.
- Use Markdown formatting.

For comparison questions, follow EXACTLY this structure:

### 🐍 Python vs Other Language

**Overview:**  
Give a 2-3 sentence overview.

### 🔹 Similarities
- Point 1
- Point 2
- Point 3

### 🔹 Key Differences

| Feature | Python | Other Language |
|---|---|---|
| Syntax | ... | ... |
| Typing | ... | ... |
| Performance | ... | ... |
| Memory Management | ... | ... |
| Learning Curve | ... | ... |

### 🐍 Python Perspective
Explain when Python is a good choice.

### 💡 Simple Example
Give a small Python example if useful.

### ✅ In Short
Give a 1-2 sentence conclusion.

IMPORTANT:
- Do not add another heading after "### ✅ In Short".
- Always finish the answer completely.
- Keep the answer within approximately 200-250 words.

Question:
{query}
"""

        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3.2:3b",
                "prompt": prompt,
                "stream": False,
                "options": {
                    "num_predict": 200
                }
            }
        )

        data = response.json()
        return data.get("response", "⚠️ No response")

    except Exception as e:
        return f"⚠️ Error: {e}"
# 🔹 Generate AI answer using Ollama
# def get_answer(query):
#     try:
#         prompt = f"""
# You are a Python expert assistant.

# Rules:
# - Assume every question is about Python programming
# - Give a clear explanation (4–6 lines)
# - Also include a simple real-world example
# - Keep it easy for students to understand
# - make the important points
# - Avoid too much technical jargon

# Question: {query}
# """

#         response = requests.post(
#             "http://localhost:11434/api/generate",
#             json={
#                 "model": "llama3",
#                 "prompt": prompt,
#                 "stream": False
#             }
#         )

#         if response.status_code != 200:
#             return "⚠️ AI server not responding."

#         data = response.json()
#         return data.get("response", "⚠️ No response generated.")

#     except Exception as e:
#         return f"⚠️ Error: {e}"

# 🔹 Main route
@app.route("/", methods=["GET", "POST"])
def home():
    result = ""

    if request.method == "POST":
        query = request.form["query"]

        # ✅ FIRST: check original query
        if not is_python_query(query):
            result = "❌ This search engine only supports Python-related queries."
        else:
            # ✅ THEN enhance query
            query = enhance_query(query)
            result = get_answer(query)

    return render_template("index.html", result=result)

# 🔹 Run server
if __name__ == "__main__":
    app.run(debug=True)

