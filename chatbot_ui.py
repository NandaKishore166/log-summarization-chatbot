from flask import Flask, render_template, request, jsonify
from preprocess import clean_logs
from extractor import extract_events
from summarizer import generate_summary
import os
app = Flask(__name__)

with open("logs.txt") as f:
    logs = f.readlines()

cleaned = clean_logs(logs)
important = extract_events(cleaned)

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

    else:
        return "Ask me about errors, warnings, or summary."

@app.route("/")
def home():
    return render_template("chat.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_msg = request.json["message"]
    reply = get_response(user_msg)
    return jsonify({"reply": reply})

if __name__ == "__main__":
port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)
