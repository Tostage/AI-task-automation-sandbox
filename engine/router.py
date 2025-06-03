def route_prompt(prompt: str) -> str:
    if "summarize" in prompt.lower():
        return "summarize"
    elif "translate" in prompt.lower():
        return "translate"
    else:
        return "general"

