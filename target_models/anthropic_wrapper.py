import anthropic

class AnthropicWrapper:
    def __init__(self, api_key: str, model: str = "claude-3-sonnet-20240229"):
        self.client = anthropic.Anthropic(api_key=api_key)
        self.model = model

    def generate(self, prompt: str, temperature: float = 0.7) -> str:
        try:
            response = self.client.messages.create(
                model=self.model,
                max_tokens=1024,
                temperature=temperature,
                messages=[{"role": "user", "content": prompt}]
            )
            return response.content[0].text.strip()
        except Exception as e:
            print(f"Anthropic API error: {e}")
            return ""
