import json
from evaluator.scoring_rules import grade_instruction_following

def evaluate_task(file_path, task_type):
    with open(file_path, 'r') as f:
        data = json.load(f)

    summary = {"✅ Fully Correct": 0, "⚠️ Partially Correct": 0, "❌ Incorrect": 0}

    for item in data:
        input_text = item.get("input", "")
        instruction = item.get("instruction", "")
        expected = item.get("expected_response")
        output = item.get("model_output")

        grade = grade_instruction_following(expected, output)
        summary[grade] += 1

        print(f"{grade} | Instruction: {instruction}")
        print(f"Expected: {expected}")
        print(f"Got: {output}\n")

    total = sum(summary.values())
    print("📊 Summary:")
    for k, v in summary.items():
        print(f"{k}: {v} ({(v / total) * 100:.1f}%)")
