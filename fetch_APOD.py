import requests
import os
import sys
from pathvalidate import sanitize_filepath
from urllib.parse import urlparse
import argparse
import urllib3
import download_img_and_return_extension
from dotenv import load_dotenv


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def fetch_APOD(img_amount, api_id):
    payloads = { 
        'count': f'{img_amount}',
        'api_key': api_id,
        }
    response = requests.get('https://api.nasa.gov/planetary/apod', params=payloads, verify=False)
    response.raise_for_status()
    os.makedirs(os.path.join('./','images'), exist_ok=True)
    for num in range(int(payloads['count'])):
        image_link = response.json()[num]["url"]
        download_img_and_return_extension.download_images(image_link, 'images', f'{num}.png')           
    return response



def main():
    load_dotenv()
    api_id = os.environ('NASA_API_ID')
    parser = argparse.ArgumentParser(
        description = 'Script downloads APOD')
    parser.add_argument('img_amount', help = 'Количество фото', default = 1, type = int)
    args = parser.parse_args()    
    try:
        APOD = fetch_APOD(args.img_amount, api_id)
    except requests.HTTPError:
        print('Фото не найдено', file=sys.stderr)


if __name__=='__main__':
    main()