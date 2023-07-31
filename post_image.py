import telegram
import os
from dotenv import load_dotenv


def post(chat_id,tg_token, doc):
    bot = telegram.Bot(token = tg_token)
    bot.send_document(chat_id = chat_id, document=doc)

