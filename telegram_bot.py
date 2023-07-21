import telegram
import os
import random
import argparse
import time




def main():
    bot = telegram.Bot(token='6102269452:AAHYMHa8CMjp_OBh_hnf2FEC4OpdVUml5Zc')
    links = os.listdir('images')
    parser = argparse.ArgumentParser(
        description = 'Script posts images')
    parser.add_argument('hours', help = 'Временной интервал публикаций', default = 4, type = int)
    args = parser.parse_args()
    sec = args.hours * 3600
    try:
        while True:
            link = random.choice(links)
            bot.send_document(chat_id='-1001933811429', document=open(f'images/{link}', 'rb'))
            time.sleep(sec)
            if not links:
                break
            links.pop(links.index[link])
    except IndexError:
        pass
  
if __name__=='__main__':
    main()