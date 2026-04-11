import psutil
from flask import Flask, render_template, request, jsonify
from preprocess import clean_logs
from extractor import extract_events
from summarizer import generate_summary
import os

app = Flask(__name__)

# Load logs safely
try:
    with open("logs.txt") as f:
        logs = f.readlines()
except:
    logs = ["No logs found"]

# Process logs
cleaned = clean_logs(logs)
important = extract_events(cleaned)

# Chatbot response logic
def get_response(user_input):
    user_input = user_input.lower()

    if "error" in user_input:
        return "\n".join([log for log in important if "error" in log.lower()]) or "No errors found."

    elif "warning" in user_input:
        return "\n".join([log for log in important if "warning" in log.lower()]) or "No warnings found."

    elif "summary" in user_input:
        return generate_summary(". ".join(important))

    elif "all logs" in user_input:
        return "\n".join(logs)
    
    elif "cpu" in user_input:
    return get_cpu()

    else:
        return "Ask me about errors, warnings, or summary."

# Home route
@app.route("/")
def home():
    return render_template("chat.html")

# Chat API
@app.route("/chat", methods=["POST"])
def chat():
    user_msg = request.json.get("message", "")
    reply = get_response(user_msg)
    return jsonify({"reply": reply})

# Run app (Render compatible)
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))   # ✅ FIXED INDENTATION
    app.run(host="0.0.0.0", port=port)
    def get_cpu():
    return f"CPU Usage: {psutil.cpu_percent()}%"

def get_memory():
    mem = psutil.virtual_memory()
    return f"Memory Usage: {mem.percent}%"

def get_disk():
    return f"Disk Usage: {psutil.disk_usage('/').percent}%"