import openai

class SafetyClassifier:
    def __init__(self, api_key=None):
        self.api_key = api_key
        openai.api_key = api_key

    def is_safe(self, text: str) -> bool:
        try:
            response = openai.Moderation.create(input=text)
            flagged = response["results"][0]["flagged"]
            return not flagged
        except Exception as e:
            print(f"Moderation API error: {e}")
            return True  # default to safe if API fails
class DummyClassifier:
    def is_safe(self, prompt: str) -> bool:
        blacklist = ["bomb", "kill", "hack", "attack", "malware"]
        return not any(word in prompt.lower() for word in blacklist)
