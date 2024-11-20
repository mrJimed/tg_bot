import os

import whisper

from config.app_config import TRANSCRIBATION_MODEL_NAME

_model = whisper.load_model(TRANSCRIBATION_MODEL_NAME)


def get_file_text(file_path: str) -> str:
    if os.path.exists(file_path):
        audio = whisper.load_audio(file_path)
        audio = whisper.pad_or_trim(audio)
        result = _model.transcribe(audio)
        return result['text']
    return ''
