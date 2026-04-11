def extract_events(logs):
    important = []
    for log in logs:
        if any(word in log.lower() for word in ["error", "warning", "critical"]):
            important.append(log)
    return important