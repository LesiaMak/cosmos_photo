import requests
import urllib3
import os
from pathvalidate import sanitize_filepath
from urllib.parse import urlparse


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def download_images(image_url, save_path, image_name, payloads = None):
    os.makedirs(os.path.join('./',save_path), exist_ok=True)
    response = requests.get(image_url, params=payloads,  verify=False)
    response.raise_for_status()
    filename = sanitize_filepath(os.path.join(save_path, f'{image_name}{return_extention(image_url)}'))
    with open(filename, 'wb') as file:
        file.write(response.content)
    return(response)


def return_extention(url):
    path = urlparse(url).path
    splited_path = os.path.split(path)[1]
    extention = os.path.splitext(splited_path)[1]
    return extention


