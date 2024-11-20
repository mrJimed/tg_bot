import os

from dotenv import dotenv_values

path = os.path.join(os.path.dirname(__file__), 'config.env')
conf = dotenv_values(path)

TG_BOT_TOKEN = conf['TG_BOT_TOKEN']
TRANSCRIBATION_MODEL_NAME = conf['TRANSCRIBATION_MODEL_NAME']
