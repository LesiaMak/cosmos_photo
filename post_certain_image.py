import telegram
import os
import random
import argparse
from dotenv import load_dotenv
from pathlib import Path
import post_image
 


def main():
    load_dotenv()
    tg_chat_id = os.environ['TG_CHAT_ID']
    links = os.listdir('images')
    parser = argparse.ArgumentParser(
        description = 'Script posts certain image')
    parser.add_argument('--image', help = 'Наименование изображения', default = random.choice(links), type = str)
    args = parser.parse_args()
    try:
        with open(Path('images', args.image), 'rb') as doc:
            post_image.post(tg_chat_id, doc)
    except IndexError:
        pass

if __name__=='__main__':
    main()