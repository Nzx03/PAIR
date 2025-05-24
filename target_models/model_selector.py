from .openai_wrapper import OpenAIWrapper
from .anthropic_wrapper import AnthropicWrapper
from .gemini_wrapper import GeminiWrapper
from .local_model import LocalModel

def get_model(config):
    model_type = config.get("model_type")

    if model_type == "openai":
        return OpenAIWrapper(config)
    elif model_type == "anthropic":
        return AnthropicWrapper(config)
    elif model_type == "gemini":
        return GeminiWrapper(config)
    elif model_type == "local":
        return LocalModel(config)
    else:
        raise ValueError(f"Unsupported model type: {model_type}")
