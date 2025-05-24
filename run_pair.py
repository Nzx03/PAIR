# import sys
# import os

# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import yaml
from attacker.pair_attacker import PAIRAttacker
from target_models.model_selector import get_model
from evaluator import SafetyClassifier

def load_config(path):                                                                           
    with open(path, 'r') as f:
        return yaml.safe_load(f)
    
def load_seed_prompts(filepath="data/prompts/seeds.txt"):
    with open(filepath, "r") as f:
        prompts = [line.strip() for line in f if line.strip()]
    return prompts


def main():
    attacker_config = load_config("configs/attacker_config.yaml")
    model_config = load_config("configs/target_model_config.yaml")

    target_model = get_model(model_config["target_model"])
    safety = SafetyClassifier(api_key=model_config["target_model"].get("api_key"))

    seed_prompts = load_seed_prompts() 

    pair = PAIRAttacker(
    target_model=target_model,
    seed_prompts=seed_prompts,
    max_iters=attacker_config["attacker"].get("max_iters", 20)
    )

    successful_jailbreaks = pair.run()
    print(f"Found {len(successful_jailbreaks)} successful jailbreak(s).")

if __name__ == "__main__":
    main()
