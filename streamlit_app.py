import streamlit as st
import json
import os
from evaluator.scoring_rules import grade_instruction_following
from evaluator.failure_explainer import explain_failure

# Load task JSON
def load_task(task_name):
    with open(f"tasks/{task_name}.json", "r") as f:
        return json.load(f)

# Grade response
def grade(task_type, expected, output):
    if task_type == "follow_instructions":
        grade = grade_instruction_following(expected, output)
        explanation = explain_failure(expected, output) if grade != "✅ Fully Correct" else "N/A"
    else:
        if expected.lower().strip() == output.lower().strip():
            grade = "✅ Fully Correct"
            explanation = "N/A"
        else:
            grade = "❌ Incorrect"
            explanation = "Does not match expected category."
    return grade, explanation

# App
st.set_page_config(page_title="LLM Task Evaluator", layout="wide")
st.title("🧠 AI Task Evaluation Framework")

# Select task file
task_files = [f.replace(".json", "") for f in os.listdir("tasks") if f.endswith(".json")]
task_name = st.selectbox("Select a Task File", task_files)

# Detect task type
if "instruction" in task_name:
    task_type = "follow_instructions"
else:
    task_type = "classification"

# Load and evaluate
data = load_task(task_name)
grades = {"✅ Fully Correct": 0, "⚠️ Partially Correct": 0, "❌ Incorrect": 0}

st.markdown("## Evaluation Results")

for i, item in enumerate(data):
    st.markdown(f"### Example {i+1}")
    input_text = item.get("input", "")
    instruction = item.get("instruction", "")
    expected = item.get("expected_response") or item.get("expected_category") or item.get("expected_priority")
    output = item.get("model_output", "")

    grade_label, explanation = grade(task_type, expected, output)
    grades[grade_label] += 1

    st.write("**Instruction:**", instruction or input_text)
    st.write("**Expected:**", expected)
    st.write("**Model Output:**", output)
    st.write("**Grade:**", grade_label)
    st.write("**Reason:**", explanation)
    st.markdown("---")

# Summary
st.markdown("## 📊 Summary")
total = sum(grades.values())
for g in grades:
    st.write(f"{g}: {grades[g]} / {total} ({(grades[g]/total)*100:.1f}%)")

