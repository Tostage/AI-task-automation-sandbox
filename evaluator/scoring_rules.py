def grade_instruction_following(expected, output):
    if isinstance(expected, list):
        matches = sum(1 for e in expected if e.lower() in output.lower())
        if matches == len(expected):
            return "✅ Fully Correct"
        elif matches > 0:
            return "⚠️ Partially Correct"
        else:
            return "❌ Incorrect"
    else:
        if expected.lower().strip() == output.lower().strip():
            return "✅ Fully Correct"
        elif expected.lower().strip() in output.lower():
            return "⚠️ Partially Correct"
        else:
            return "❌ Incorrect"
