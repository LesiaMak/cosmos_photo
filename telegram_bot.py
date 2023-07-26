import telegram
import os
import random
import argparse
import time
from pathlib import Path
from dotenv import load_dotenv


def post_image(chat_id, doc):
    bot = telegram.Bot(token = os.environ['TELEGRAM_TOKEN'])
    bot.send_document(chat_id = chat_id, document=doc)
    return bot


def main():
    load_dotenv()
    tg_chat_id = os.environ['TG_CHAT_ID']
    links = os.listdir('images')
    parser = argparse.ArgumentParser(
        description = 'Script posts images')
    parser.add_argument('hours', help = 'Временной интервал публикаций', default = 4, type = int)
    args = parser.parse_args()
    sec = args.hours 
    try:
        while True:
            link = random.choice(links)
            with open(Path('images', link), 'rb') as doc:
                post_image(tg_chat_id, doc)
            time.sleep(sec)
            if not links:
                break
            links.pop(links.index(link))
    except IndexError:
        pass
  
if __name__=='__main__':
    main()