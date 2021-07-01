from urllib.parse import urlparse
import random

import urllib3
import requests

import download_image


def get_current_comics_num():
    current_comics_url = "http://xkcd.com/info.0.json"
    response = requests.get(current_comics_url)
    response.raise_for_status()
    return response.json()["num"]


def get_comics_metadata(comics_endpoint_url):
    response = requests.get(comics_endpoint_url)
    response.raise_for_status()
    comics_metadata = response.json()
    return comics_metadata


def fetch_comics_img():
    comics_url = comics_metadata["img"]
    parsed_img_url = urlparse(comics_url)
    # При парсинге url комикса path включает в себя подраздел comics,
    # поэтому делаем для него replace для правильного обращения к файлу
    filename = parsed_img_url.path.replace("/comics/", "")
    download_image.download_image(comics_url, filename)
    return filename


def fetch_comics_comment():
    comics_comment = comics_metadata["alt"]
    return comics_comment


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
comics_num = random.randint(1, get_current_comics_num())
comics_endpoint_url = f"https://xkcd.com/{comics_num}/info.0.json"
comics_metadata = get_comics_metadata(comics_endpoint_url)
