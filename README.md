# AI-task-automation-sandbox

This project simulates real-world microtasks used in AI operations platforms (e.g., Outlier, Surge, Invisible). It includes logic-based classification, instruction-following tasks and auto-evaluation scripts. Designed to showcase how prompts, outputs and evaluation logic can be combined for consistent automation.

## 🧠 Tasks Simulated

- **Email Classification**: Assign categories like "Support", "Sales" or "Spam" to sample emails.
- **Ticket Triage**: Prioritize support tickets based on urgency and issue type.
- **Instruction Following QA**: Judge if answers fully, partially or fail to follow instructions.

## 📂 Structure

- `tasks/`: Contains JSON datasets with prompts, LLM outputs, and target answers.
- `evaluate.py`: Evaluates outputs based on simple logical rules.
- `run_task.py`: Loads task files, prints task outputs and runs evaluations.

## 🔧 Example Usage

```bash
python run_task.py --task classify_emails
