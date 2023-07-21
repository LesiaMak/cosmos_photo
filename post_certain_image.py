import telegram
import os
import random
import argparse



def post_photo(image_link):
    bot.send_document(chat_id='-1001933811429', document=open(f'images/{image_link}', 'rb'))



def main():
    bot = telegram.Bot(token='6102269452:AAHYMHa8CMjp_OBh_hnf2FEC4OpdVUml5Zc')
    links = os.listdir('images')
    parser = argparse.ArgumentParser(
        description = 'Script posts certain image')
    parser.add_argument('image', help = 'Наименование изображения', default = random.choice(links), type = str)
    args = parser.parse_args()
    try:
        post_photo(args.image)
    except IndexError:
        pass

if __name__=='__main__':
    main()