import json
from evaluator.scoring_rules import grade_instruction_following
from evaluator.failure_explainer import explain_failure

def evaluate_task(file_path, task_type, use_gpt=False):
    with open(file_path, "r") as f:
        data = json.load(f)

    summary = {
        "✅ Fully Correct": 0,
        "⚠️ Partially Correct": 0,
        "❌ Incorrect": 0
    }

    for item in data:
        input_text = item.get("input", "")
        instruction = item.get("instruction", "")
        output = item.get("model_output", "")
        expected = (
            item.get("expected_response") or
            item.get("expected_category") or
            item.get("expected_priority")
        )

        # Choose grading logic based on task type
        if task_type == "follow_instructions":
            grade = grade_instruction_following(expected, output)
        else:
            # Simple equality check for classification-style tasks
            if output and expected and output.strip().lower() == expected.strip().lower():
                grade = "✅ Fully Correct"
            else:
                grade = "❌ Incorrect"

        explanation = explain_failure(expected, output) if grade != "✅ Fully Correct" else "N/A"
        summary[grade] += 1

        print("=" * 60)
        print(f"{grade} | Input: {input_text or instruction}")
        print(f"Expected: {expected}")
        print(f"Got     : {output}")
        print(f"Reason  : {explanation}\n")

    total = sum(summary.values())
    print("\n📊 Final Summary:")
    for k, v in summary.items():
        print(f"{k}: {v} / {total} ({(v / total) * 100:.1f}%)")
