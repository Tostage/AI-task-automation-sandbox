from engine.local_llm import run_prompt

def execute_task(prompt: str, task_type: str) -> str:
    if task_type == "summarize":
        formatted = f"Summarize this:\n\n{prompt}"
    elif task_type == "translate":
        formatted = f"Translate to French:\n\n{prompt}"
    else:
        formatted = prompt
    return run_prompt(formatted)

