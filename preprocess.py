import re

def clean_logs(logs):
    cleaned = []
    for log in logs:
        log = re.sub(r"\[.*?\]", "", log)
        log = re.sub(r"[^a-zA-Z0-9\s]", "", log)
        cleaned.append(log.strip())
    return cleaned
