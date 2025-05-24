import json
from evaluator.metrics import (
    evaluate_jailbreak_success,
    evaluate_fluency,
    evaluate_transferability
)

def load_results(path):
    with open(path, 'r') as f:
        return [json.loads(line) for line in f]

def main():
    results = load_results(r"C:\Users\Nazneen\git\PAIR\data\jailbreaks\jailbreaks.jsonl")

    success_count = 0
    fluency_scores = []
    for entry in results:
        output = entry.get("model_output", "")
        if evaluate_jailbreak_success(output):
            success_count += 1
        fluency_scores.append(evaluate_fluency(output))

    print(f"Jailbreak Success Rate: {success_count / len(results):.2f}")
    print(f"Average Fluency Score: {sum(fluency_scores)/len(fluency_scores):.2f}")

if __name__ == "__main__":
    main()
