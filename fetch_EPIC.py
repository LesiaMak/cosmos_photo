import requests
import os
import urllib3
import sys
import argparse
import datetime
import download_img_and_return_extension
from dotenv import load_dotenv


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def fetch_EPIC(img_num, api_id):
    for i in range(1, img_num):
        day = datetime.datetime(year=2018, month=5, day=30) + datetime.timedelta(days=i)
        date = day.strftime("%Y/%m/%d")
        payloads = {
            'api_key': api_id,
        }
        response = requests.get(f'https://api.nasa.gov/EPIC/api/natural/date/{day}', params=payloads, verify=False)
        response.raise_for_status()
        image_name = response.json()[-1]['image']
        image_link = f'https://api.nasa.gov/EPIC/archive/natural/{date}/png/{image_name}.png'
        download_img_and_return_extension.download_images(image_link, 'images', image_name, payloads=payloads)
    return response


def main():
    load_dotenv()
    api_id = os.environ('NASA_API_ID')
    parser = argparse.ArgumentParser(
        description = 'Script downloads EPIC')
    parser.add_argument('amount', help = 'Количество фото', default = 1, type = int)
    args = parser.parse_args()
   
    try:
        APOD = fetch_EPIC(args.amount, api_id)
    except requests.HTTPSError:
        print('Фото не найдено', file=sys.stderr)


if __name__=='__main__':
    main()