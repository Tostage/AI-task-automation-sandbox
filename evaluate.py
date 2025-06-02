import json
from scoring_rules import score_output

def evaluate_task(file_path, task_type, use_gpt=False):
    with open(file_path, 'r') as f:
        data = json.load(f)

    results = []

    for item in data:
        instruction = item.get("instruction", "")
        input_text = item.get("input", "")
        expected_points = item["expected_points"]
        model_output = item["model_output"]

        score, label, hits = score_output(expected_points, model_output)
        item["score"] = score
        item["evaluator_comment"] = label

        print(f"{label} | Score: {score:.2f}")
        print(f"Instruction: {instruction}")
        print(f"Output: {model_output}")
        print(f"Matched {hits}/{len(expected_points)} key points\n")

        results.append(item)

    # Optional: write back results
    with open(file_path.replace(".json", "_scored.json"), "w") as f:
        json.dump(results, f, indent=2)
