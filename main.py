import json
from engine.router import route_prompt
from engine.executor import execute_task
from engine.evaluate import evaluate_task

with open("data/tasks.json") as f:
    tasks = json.load(f)

results = []

for task in tasks:
    prompt = task["prompt"]
    task_type = route_prompt(prompt)
    response = execute_task(prompt, task_type)
    evaluation = evaluate_task(prompt, response)

    print(f"\n🟡 Prompt: {prompt}")
    print(f"🟢 Response: {response}")
    print(f"🔍 Verdict: {evaluation['verdict']} ({evaluation['confidence']}%) — {evaluation['explanation']}")
    print('-' * 80)

    results.append({
        "prompt": prompt,
        "response": response,
        "verdict": evaluation["verdict"],
        "confidence": evaluation["confidence"],
        "explanation": evaluation["explanation"]
    })

# Save all run results
with open("data/results.json", "w") as f:
    json.dump(results, f, indent=2)
