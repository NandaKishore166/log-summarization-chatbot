def generate_summary(text):
    if not text:
        return "No important logs found."

    errors = text.lower().count("error")
    warnings = text.lower().count("warning")

    return f"Summary: {errors} errors, {warnings} warnings detected in logs."