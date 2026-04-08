from flask import Flask, render_template
from preprocess import clean_logs
from extractor import extract_events
from summarizer import generate_summary

app = Flask(__name__)

def process_logs():
    with open("logs.txt") as f:
        logs = f.readlines()

    cleaned = clean_logs(logs)
    important = extract_events(cleaned)
    summary = generate_summary(". ".join(important))

    return important, summary

@app.route("/")
def home():
    important, summary = process_logs()
    return render_template("index.html", logs=important, summary=summary)

if __name__ == "__main__":
    app.run(debug=True)
