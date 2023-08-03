import telegram
import os
import argparse
import time
import sys
from dotenv import load_dotenv
import post_image


def main():
    load_dotenv()
    tg_chat_id = os.environ['TG_CHAT_ID']
    token = os.environ['TELEGRAM_TOKEN']
    links = os.listdir('images')
    parser = argparse.ArgumentParser(
        description = 'Script posts images')
    parser.add_argument('--sec', help = 'Временной интервал публикаций', default = 4, type = int)
    args = parser.parse_args()
    try:
        while links:
            for link in links:            
                post_image.post_doc('images', link, tg_chat_id, token )
                links.pop(links.index(link))
                time.sleep(args.sec)
        else:
            links = os.listdir('images')
                                               
    except IndexError:
        print('Фото не найдено', file=sys.stderr)
    except telegram.error.NetworkError:
        print('Нет связи с сервером', file=sys.stderr)
    
  
if __name__=='__main__':
    main()