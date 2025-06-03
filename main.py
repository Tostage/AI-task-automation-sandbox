import json  # ← THIS LINE WAS MISSING

from engine.router import route_prompt
from engine.executor import execute_task

with open("data/tasks.json") as f:
    tasks = json.load(f)

for task in tasks:
    prompt = task["prompt"]
    task_type = route_prompt(prompt)
    result = execute_task(prompt, task_type)
    print(f"\n🟡 Prompt: {prompt}\n🟢 Output: {result}\n{'-'*60}")
