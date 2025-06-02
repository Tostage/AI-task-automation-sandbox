import json
import os
from openai import OpenAI

client = OpenAI()  # Uses OPENAI_API_KEY from environment

def get_model_output(task_type, input_text, instruction=None):
    if task_type == "follow_instructions":
        prompt = f"Instruction: {instruction}\nInput: {input_text}\nAnswer:"
    else:
        prompt = f"Input: {input_text}\nCategory:"

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )

    return response.choices[0].message.content.strip()

def evaluate_task(file_path, task_type, use_gpt=False):
    with open(file_path, 'r') as f:
        data = json.load(f)

    correct = 0
    for item in data:
        input_text = item.get("input", "")
        instruction = item.get("instruction", "")

        if use_gpt:
            output = get_model_output(task_type, input_text, instruction)
            item["model_output"] = output
        else:
            output = item["model_output"]

        expected = item.get("expected_category") or item.get("expected_priority") or item.get("expected_response")

        # Simple match logic
        if isinstance(expected, list):
            match = all(e.lower() in output.lower() for e in expected)
        else:
            match = output.strip().lower() == expected.strip().lower()

        result = "✅" if match else "❌"
        if match:
            correct += 1

        print(f"{result} Input: {input_text}")
        print(f"  Expected: {expected} | Got: {output}\n")

    print(f"\nAccuracy: {correct}/{len(data)} correct ({(correct / len(data)) * 100:.1f}%)")
