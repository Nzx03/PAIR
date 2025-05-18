from google.generativeai import GenerativeModel, configure

class GeminiWrapper:
    def __init__(self, api_key: str, model_name: str = "gemini-pro"):
        self.api_key = api_key
        self.model_name = model_name
        configure(api_key=api_key)
        self.model = GenerativeModel(model_name)

    def generate(self, prompt: str, temperature: float = 0.7) -> str:
        try:
            response = self.model.generate_content(
                prompt,
                generation_config={"temperature": temperature}
            )
            return response.text.strip()
        except Exception as e:
            print(f"Gemini API error: {e}")
            return ""

