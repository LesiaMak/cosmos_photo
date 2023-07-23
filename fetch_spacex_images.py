import requests
import urllib3
import os
import sys
from urllib.parse import urlparse
import argparse
import download_img_and_return_extention



def fetch_spacex_launch(launch_id):
    response = requests.get(f'https://api.spacexdata.com/v5/launches/{launch_id}', verify=False)
    response.raise_for_status()
    image_links = response.json()['links']['flickr']['original']
    for image_number, link in enumerate(image_links):
        download_img_and_return_extention.download_images(link, 'images', f'spaceex{image_number}')
    return response


def main():
    parser = argparse.ArgumentParser(
        description = 'Script downloads image of SpaceX launches')
    parser.add_argument('launch_id', help='ID запуска', default='latest', type = str)
    args = parser.parse_args()
    try:
        launch = fetch_spacex_launch(args.launch_id)
    except requests.HTTPError:
        print('Запуск не найден. Введите другой ID', file=sys.stderr)
    except requests.ConnectionError:
        print('Нет связи с сервером', file=sys.stderr)



if __name__=='__main__':
    main()