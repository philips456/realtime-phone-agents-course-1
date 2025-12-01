from realtime_phone_agents.tts.models.base import TTSModel
from realtime_phone_agents.tts.models.kokoro import KokoroTTSModel
from realtime_phone_agents.tts.models.orpheus_runpod import OrpheusTTSModel


def get_tts_model(model_name: str) -> TTSModel:
    """Get a TTS model by name."""
    if model_name == "kokoro":
        return KokoroTTSModel()
    elif model_name == "orpheus-runpod":
        return OrpheusTTSModel()
    else:
        raise ValueError(f"Invalid TTS model name: {model_name}")
