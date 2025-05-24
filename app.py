import streamlit as st
import json
from evaluator.metrics import (
    evaluate_jailbreak_success,
    evaluate_fluency,
    evaluate_transferability
)

# Load results (jsonl file: one JSON object per line)
def load_results(path):
    results = []
    with open(path, 'r') as f:
        for line in f:
            if line.strip():
                results.append(json.loads(line))
    return results

def main():
    st.title("Jailbreak Evaluation Dashboard")

    # File path or upload
    file_path = st.text_input("Enter path to jailbreaks JSONL file", 
                             value=r"C:\Users\Nazneen\git\PAIR\data\jailbreaks\jailbreaks.jsonl")

    if st.button("Load and Evaluate"):
        try:
            results = load_results(file_path)
            if not results:
                st.warning("No data found in the file!")
                return

            success_count = 0
            fluency_scores = []
            for entry in results:
                output = entry.get("response", "")  # Adjust if your key is different
                if evaluate_jailbreak_success(output):
                    success_count += 1
                fluency_scores.append(evaluate_fluency(output))

            st.write(f"**Total Samples:** {len(results)}")
            st.write(f"**Jailbreak Success Rate:** {success_count / len(results):.2%}")
            st.write(f"**Average Fluency Score:** {sum(fluency_scores) / len(fluency_scores):.2f}")

            # Show table of results
            st.subheader("Jailbreak Attempts")
            for i, entry in enumerate(results):
                with st.expander(f"Attempt #{i+1} - Seed: {entry.get('seed_prompt', 'N/A')}"):
                    st.json(entry)

        except Exception as e:
            st.error(f"Error loading or evaluating data: {e}")

if __name__ == "__main__":
    main()
