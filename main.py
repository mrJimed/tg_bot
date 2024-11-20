import telebot
from telebot.types import Message

import helper
import transcribation
from config.app_config import TG_BOT_TOKEN

bot = telebot.TeleBot(TG_BOT_TOKEN)


@bot.message_handler(content_types=['voice'])
def speech_to_text(message: Message) -> None:
    file_id = message.voice.file_id
    file_path = helper.save_tg_file(file_id, bot)
    text_tran = transcribation.get_file_text(file_path)
    helper.remove_file(file_path)
    bot.send_message(message.from_user.id, text_tran)


bot.polling(none_stop=True, interval=0)
