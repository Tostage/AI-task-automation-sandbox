def score_output(expected_points, model_output):
    hits = sum(1 for point in expected_points if point.lower() in model_output.lower())
    total = len(expected_points)
    score = hits / total

    if score == 1:
        label = "✅ Fully correct"
    elif score >= 0.5:
        label = "⚠️ Partially correct"
    else:
        label = "❌ Incorrect"

    return score, label, hits


