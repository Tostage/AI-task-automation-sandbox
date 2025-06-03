# 🧠 AI Task Automation Sandbox

A lightweight, local task execution engine using the **Mistral LLM** via `Ollama`.

## ✅ Features
- 🧠 Free, local large language model (Mistral 7B via Ollama)
- 📥 Reads prompt tasks from `tasks.json`
- 🛠️ Routes prompts to appropriate logic (e.g. translation, summarization)
- 🚀 Executes via Mistral with no OpenAI dependency

## 📂 File Structure
AI-task-automation-sandbox/
├── main.py # CLI runner
├── engine/
│ ├── local_llm.py # Local LLM runner using Ollama
│ ├── router.py # Task type router
│ └── executor.py # Routes prompt + formats query
├── data/
│ └── tasks.json # Prompt input
├── requirements.txt # Dependencies

## ▶️ How to Run
1. **Start the Mistral model:**
ollama run mistral
2. **In another terminal:**
python main.py
3. 🔁 Model processes 10 prompts from `data/tasks.json`
4. pip install -r requirements.txt
