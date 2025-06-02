import argparse
from evaluate import evaluate_task

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--task", type=str, required=True, help="Task name (no extension)")
    parser.add_argument("--use_gpt", action="store_true", help="Generate outputs with GPT-4")

    args = parser.parse_args()

    task_file = f"tasks/{args.task}.json"
    evaluate_task(task_file, args.task, use_gpt=args.use_gpt)
