import urllib3

import requests


def download_image(url, filename):
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    response = requests.get(url, verify=False)
    response.raise_for_status()
    with open(filename, "wb") as image:
        image.write(response.content)
