# PAIR-Adversarial-LLM 🔐🤖

This project implements **PAIR (Prompt Automatic Iterative Refinement)** to generate adversarial jailbreak prompts against LLMs like GPT-4, Claude, and Gemini, and evaluates their defenses.

---

## 📁 Project Structure

- `attacker/` – Logic to generate and refine adversarial prompts
- `target_models/` – Interfaces for OpenAI, Anthropic, Gemini, and local models
- `evaluator/` – Safety classifier, evaluation metrics
- `data/` – Prompts, jailbreaks, logs
- `scripts/` – Main entry points for running attack or evaluation
- `notebooks/` – Visualizations and debugging
- `tests/` – Unit tests

---

## 🚀 Getting Started

1. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

2. **Run PAIR attack:**
    ```bash
    python run_pair.py --config configs/attacker_config.yaml
    ```

3. **Evaluate generated jailbreak prompts**
    ```bash
    python eval_jailbreaks.py
    ```

4. **Launch the Streamlit Dashboard**
    ```bash
    streamlit run app.py
    ```

---

