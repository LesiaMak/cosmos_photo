import telegram
import os
import random
import argparse
from dotenv import load_dotenv

load_dotenv()

def main():
    bot = telegram.Bot(token=os.getenv('TOKEN'))
    links = os.listdir('images')
    parser = argparse.ArgumentParser(
        description = 'Script posts certain image')
    parser.add_argument('image', help = 'Наименование изображения', default = random.choice(links), type = str)
    args = parser.parse_args()
    try:
        with open(f'images/{args.image}', 'rb') as doc:
            bot.send_document(chat_id=os.getenv('CHAT_ID'), document=doc)
    except IndexError:
        pass

if __name__=='__main__':
    main()