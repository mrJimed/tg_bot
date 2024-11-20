import uuid

from telebot import TeleBot


def save_tg_file(file_id: str, bot: TeleBot) -> str:
    file_name = f'audio/{uuid.uuid4().hex}.wav'
    file = bot.get_file(file_id)
    file_bytes = bot.download_file(file.file_path)
    with open(file_name, 'wb') as f:
        f.write(file_bytes)
    return file_name
