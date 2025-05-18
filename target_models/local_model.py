from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
import torch

class LocalModel:
    def __init__(self, model_name: str = "gpt2"):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name)
        self.pipeline = pipeline("text-generation", model=self.model, tokenizer=self.tokenizer)

    def generate(self, prompt: str, temperature: float = 0.7, max_new_tokens: int = 150) -> str:
        try:
            outputs = self.pipeline(prompt, do_sample=True, temperature=temperature, max_new_tokens=max_new_tokens)
            return outputs[0]["generated_text"].strip()
        except Exception as e:
            print(f"Local model error: {e}")
            return ""