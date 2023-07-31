import telegram
import os
import random
import argparse
import time
from pathlib import Path
from dotenv import load_dotenv
import post_image


def main():
    load_dotenv()
    tg_chat_id = os.environ['TG_CHAT_ID']
    token = os.environ['TELEGRAM_TOKEN']
    links = os.listdir('images')
    parser = argparse.ArgumentParser(
        description = 'Script posts images')
    parser.add_argument('--hours', help = 'Временной интервал публикаций', default = 4, type = int)
    args = parser.parse_args()
    sec = args.hours 
    try:
        while True:
            link = random.choice(links)
            with open(Path('images', link), 'rb') as doc:
                post_image.post(tg_chat_id, token, doc)
            time.sleep(sec)
            if not links:
                break
            links.pop(links.index(link))
    except IndexError:
        pass
  
if __name__=='__main__':
    main()