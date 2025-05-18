# tests/test_attacker.py

import pytest
from attacker.pair_attacker import PAIRAttacker
from target_models.local_model import LocalModel
from evaluator.safety_classifier import DummyClassifier

def test_pair_attack_returns_string():
    target = LocalModel()
    classifier = DummyClassifier()
    attacker = PAIRAttacker(target_model=target, config={}, classifier=classifier)

    benign_prompt = "How do I grow tomatoes?"
    jailbreak_prompt, metadata = attacker.attack(benign_prompt)

    assert isinstance(jailbreak_prompt, str)
    assert "attempts" in metadata
    assert metadata["attempts"] > 0
