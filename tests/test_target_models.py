# tests/test_target_models.py

import pytest
from target_models.local_model import LocalModel

def test_local_model_generates_response():
    model = LocalModel()
    prompt = "What is the capital of France?"
    response = model.generate(prompt)
    
    assert isinstance(response, str)
    assert len(response) > 0
    assert "Paris" in response or "France" in response
