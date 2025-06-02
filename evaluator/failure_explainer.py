def explain_failure(expected, output):
    if not output:
        return "No response provided."

    if isinstance(expected, list):
        matched = [e for e in expected if e.lower() in output.lower()]
        missing = [e for e in expected if e.lower() not in output.lower()]

        if len(matched) == 0:
            return "None of the expected points were mentioned."
        elif len(matched) < len(expected):
            return f"Only covered {len(matched)} of {len(expected)} required points. Missing: {missing}"
        else:
            return "N/A"
    else:
        if expected.lower().strip() == output.lower().strip():
            return "N/A"
        elif expected.lower().strip() in output.lower():
            return "Too vague — only partially matched expected phrasing."
        else:
            return "Output doesn't match or resemble the expected response."

