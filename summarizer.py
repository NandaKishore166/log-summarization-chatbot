from transformers import pipeline

summarizer = pipeline("text-generation", model="gpt2")

def generate_summary(text):
    if not text:
        return "No important logs found."
    
    # simple fast summary
    sentences = text.split(".")
    return " | ".join(sentences[:2])
