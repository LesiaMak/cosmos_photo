import requests
import os
import sys
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
    APODs = response.json()
    for image_num, APOD in enumerate(APODs):
        download_img_and_return_extension.download_images(APOD["url"], 'images', f'{image_num}')


def main():
    load_dotenv()
    api_id = os.environ['NASA_API_TOKEN']
    parser = argparse.ArgumentParser(
        description='Script downloads APOD')
    parser.add_argument('--img_amount', help='Количество фото', default=5, type=int)
    args = parser.parse_args()
    try:
        fetch_APOD(args.img_amount, api_id)
    except requests.HTTPError:
        print('Фото не найдено', file=sys.stderr)


if __name__ == '__main__':
    main()

