from realtime_phone_agents.stt.models.whisper_groq import WhisperGroqSTT
from realtime_phone_agents.stt.models.moonshine import MoonshineSTT
from realtime_phone_agents.stt.models.faster_whisper import FasterWhisperSTT
from realtime_phone_agents.stt.models.base import STTModel


def get_stt_model(model: str) -> STTModel:
    """Get the STT model based on the model name."""
    if model == "moonshine":
        return MoonshineSTT()
    elif model == "whisper-groq":
        return WhisperGroqSTT()
    elif model == "faster-whisper":
        return FasterWhisperSTT()
    else:
        raise ValueError(f"Invalid model: {model}")
