from transformers import pipeline

summarizer = pipeline("text-generation", model="gpt2")

def generate_summary(text):
    if len(text.strip()) == 0:
        return "No important logs found."

    prompt = "Summarize this log data: " + text

    result = summarizer(prompt, max_length=100, num_return_sequences=1)
    return result[0]['generated_text']
