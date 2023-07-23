import requests
import os
import sys
from pathvalidate import sanitize_filepath
from urllib.parse import urlparse
import argparse
import urllib3
from dotenv import load_dotenv

load_dotenv()
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
        r = requests.get(image_link, verify=False)
        r.raise_for_status()
        filename = sanitize_filepath(os.path.join('images', f'{num}.png'))
        with open(filename, 'wb') as file:
            file.write(r.content)                     
    return response

def main():
    parser = argparse.ArgumentParser(
        description = 'Script downloads APOD')
    parser.add_argument('img_amount', help = 'Количество фото', default = 1, type = int)
    args = parser.parse_args()
    api_id = os.getenv('API_ID')
    try:
        APOD = fetch_APOD(args.img_amount, api_id)
    except requests.HTTPError:
        print('Фото не найдено', file=sys.stderr)


if __name__=='__main__':
    main()