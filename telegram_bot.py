import telegram
import os
import random
import argparse
import time
from dotenv import load_dotenv

load_dotenv()


def main():
    bot = telegram.Bot(token = os.getenv('TOKEN'))
    links = os.listdir('images')
    parser = argparse.ArgumentParser(
        description = 'Script posts images')
    parser.add_argument('hours', help = 'Временной интервал публикаций', default = 4, type = int)
    args = parser.parse_args()
    sec = args.hours * 3600
    try:
        while True:
            link = random.choice(links)
            bot.send_document(chat_id = os.getenv('CHAT_ID'), document=open(f'images/{link}', 'rb'))
            time.sleep(sec)
            if not links:
                break
            links.pop(links.index[link])
    except IndexError:
        pass
  
if __name__=='__main__':
    main()