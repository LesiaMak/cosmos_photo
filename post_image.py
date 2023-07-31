import telegram
import os
from dotenv import load_dotenv


def post(chat_id, doc):
    bot = telegram.Bot(token = os.environ['TELEGRAM_TOKEN'])
    bot.send_document(chat_id = chat_id, document=doc)

