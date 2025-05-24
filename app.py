import streamlit as st
import subprocess
import json
import os
from evaluator.metrics import evaluate_jailbreak_success, evaluate_fluency

st.set_page_config(page_title="PAIR Jailbreak Evaluator", layout="wide")
st.title("🔐 PAIR – Adversarial Prompt Generator & Evaluator")

# Step 1: Run PAIR Attack
st.header("⚔️ 1. Generate Jailbreak Prompts")
config_path = st.text_input("Path to Attacker Config File", value="configs/attacker_config.yaml")

if st.button("Run PAIR Attack"):
    with st.spinner("Running attack..."):
        try:
            subprocess.run(["python", "run_pair.py", "--config", config_path], check=True)
            st.success("Attack completed successfully.")
        except subprocess.CalledProcessError as e:
            st.error("Attack script failed.")
            st.exception(e)

# Step 2: Evaluate Results
st.header("📊 2. Evaluate Jailbreak Results")
jailbreak_file = st.text_input("Path to generated .jsonl results file", value="data/jailbreaks/jailbreaks.jsonl")

if st.button("Run Evaluation"):
    if not os.path.exists(jailbreak_file):
        st.error(f"File not found: {jailbreak_file}")
    else:
        with open(jailbreak_file, 'r') as f:
            results = [json.loads(line) for line in f if line.strip()]

        success_count = 0
        fluency_scores = []

        for entry in results:
            output = entry.get("response", "")
            if evaluate_jailbreak_success(output):
                success_count += 1
            fluency_scores.append(evaluate_fluency(output))

        st.metric("✅ Jailbreak Success Rate", f"{success_count / len(results):.2%}")
        st.metric("🗣️ Average Fluency Score", f"{sum(fluency_scores) / len(fluency_scores):.2f}")

        st.subheader("📄 Sample Outputs")
        for i, entry in enumerate(results[:5]):
            st.markdown(f"**Prompt {i+1}:** `{entry.get('final_prompt')}`")
            st.code(entry.get("response", "No response"))
