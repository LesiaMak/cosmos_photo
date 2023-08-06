import telegram
from pathlib import Path


def post_doc(folder, image_name, tg_chat_id, token):
    with open(Path(folder, image_name), 'rb') as doc:
        post(tg_chat_id, token, doc)


def post(chat_id, tg_token, doc):
    bot = telegram.Bot(token=tg_token)
    bot.send_document(chat_id=chat_id, document=doc)



