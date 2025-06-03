import requests

def evaluate_task(prompt: str, response: str) -> dict:
    eval_prompt = f"""Evaluate the following:

Prompt:
{prompt}

Response:
{response}

Is this response relevant and accurate? Answer with:
- verdict: ✅ or ❌
- confidence: % score from 0 to 100
- explanation: 1-sentence justification
"""

    res = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": "mistral", "prompt": eval_prompt, "stream": False}
    )

    raw = res.json()["response"]

    # Fallback parser (could vary a bit)
    verdict = "✅" if "✅" in raw else "❌"
    confidence = next((int(s) for s in raw.split() if s.strip('%').isdigit()), 50)
    explanation = raw.strip().split('\n')[-1]

    return {
        "verdict": verdict,
        "confidence": confidence,
        "explanation": explanation.strip()
    }
