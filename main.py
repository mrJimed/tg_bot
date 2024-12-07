import telebot
from telebot.types import Message

import helper
import summarization
import transcribation
from config.app_config import TG_BOT_TOKEN

bot = telebot.TeleBot(TG_BOT_TOKEN)


@bot.message_handler(commands=['start'])
def start_message(message: Message):
    bot.send_message(message.from_user.id,
                     'Здравствуйте! Данный бот предназначен для генерации краткой текстовой аннотации аудио и текстового контента в Telegram. Чтобы получить аннотацию отправьте мне текстовое или аудио сообщение.')


@bot.message_handler(content_types=['voice'])
def annotation_audio(message: Message) -> None:
    file_id = message.voice.file_id
    file_path = helper.save_tg_file(file_id, bot)
    text_tran = transcribation.get_file_text(file_path)
    helper.remove_file(file_path)
    annotation = summarization.summarize_text(text_tran)
    bot.send_message(message.from_user.id, annotation)


@bot.message_handler(content_types=['text'])
def annotation_text(message: Message) -> None:
    annotation = summarization.summarize_text(message.text)
    bot.send_message(message.from_user.id, annotation)


bot.polling(none_stop=True, interval=0)
