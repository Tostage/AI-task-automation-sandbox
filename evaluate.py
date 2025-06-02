import json
import sys

def evaluate_task(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)

    correct = 0
    for item in data:
        if item["model_output"].strip().lower() == item["expected_category"].strip().lower():
            result = "✅"
            correct += 1
        else:
            result = "❌"
        print(f"{result} Input: {item['input']}")
        print(f"  Expected: {item['expected_category']} | Got: {item['model_output']}\n")

    print(f"\nAccuracy: {correct}/{len(data)} correct ({(correct / len(data)) * 100:.1f}%)")

if __name__ == "__main__":
    task_file = sys.argv[1] if len(sys.argv) > 1 else "tasks/classify_emails.json"
    evaluate_task(task_file)

