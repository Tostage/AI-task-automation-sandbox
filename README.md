# AI Task Evaluation Framework

This project simulates and scores instruction-following and classification tasks using real or simulated LLM responses (e.g. ChatGPT). It is designed to reflect the kind of manual and automated evaluation work required by AI ops platforms such as Outlier, Surge, and Invisible Technologies.

---

## 🔍 Project Purpose

To evaluate how accurately LLMs follow instructions, respond to classification prompts, and deliver structured outputs.

Supports:
- Manual or GPT-generated responses
- Tiered scoring (Fully correct / Partially correct / Incorrect)
- Custom scoring logic per task type
- Evaluation summaries and task-by-task grading

---

## 🧠 Task Types

### 1. Classification (`classify_emails.json`)
Prompts the LLM to categorize inputs into one of several predefined labels (e.g. "Sales", "Support", "Escalation").

```json
{
  "input": "I need help resetting my password.",
  "expected_category": "Support",
  "model_output": "Support"
}
