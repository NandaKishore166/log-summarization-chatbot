def extract_events(logs):
    keywords = ["error", "warning", "fail", "critical"]
    important = []

    for log in logs:
        if any(k in log.lower() for k in keywords):
            important.append(log)

    return important
