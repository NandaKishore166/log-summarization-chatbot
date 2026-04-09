def generate_summary(text):
    if not text:
        return "No important logs found."

    # simple fast summary
    sentences = text.split(".")
    return " | ".join(sentences[:2])