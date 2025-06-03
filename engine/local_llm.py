import requests

def run_prompt(prompt: str) -> str:
    res = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": "mistral", "prompt": prompt, "stream": False}
    )
    return res.json()["response"]

