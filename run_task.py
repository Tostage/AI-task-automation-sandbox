import argparse
from evaluate import evaluate_task

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--task", type=str, required=True, help="Name of task JSON file (no extension)")
    args = parser.parse_args()

    file_path = f"tasks/{args.task}.json"
    evaluate_task(file_path)

