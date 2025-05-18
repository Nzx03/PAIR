import yaml
from attacker.pair import PAIRAttacker
from target_models import get_model
from evaluator import SafetyClassifier

def load_config(path):
    with open(path, 'r') as f:
        return yaml.safe_load(f)

def main():
    attacker_config = load_config("configs/attacker_config.yaml")
    model_config = load_config("configs/target_model_config.yaml")

    target_model = get_model(model_config["target_model"])
    safety = SafetyClassifier(api_key=model_config["target_model"].get("api_key"))

    pair = PAIRAttacker(config=attacker_config["attacker"],
                        target_model=target_model,
                        safety_classifier=safety)
    
    pair.run()

if __name__ == "__main__":
    main()
