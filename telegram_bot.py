import telegram
import os
import random
import argparse
import time
from dotenv import load_dotenv


def main():
    load_dotenv()
    bot = telegram.Bot(token = os.environ('TELEGRAM_TOKEN'))
    links = os.listdir('images')
    parser = argparse.ArgumentParser(
        description = 'Script posts images')
    parser.add_argument('hours', help = 'Временной интервал публикаций', default = 4, type = int)
    args = parser.parse_args()
    sec = args.hours 
    try:
        while True:
            link = random.choice(links)
            with open(f'images/{link}', 'rb') as doc:
                bot.send_document(chat_id = os.getenv('TG_CHAT_ID'), document=doc)
            time.sleep(sec)
            if not links:
                break
            links.pop(links.index(link))
    except IndexError:
        pass
  
if __name__=='__main__':
    main()