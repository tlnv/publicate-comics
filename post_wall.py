import requests
import os
from dotenv import load_dotenv


load_dotenv()
vk_token = os.getenv("VK_ACCESS_TOKEN")
vk_group_id = os.getenv("VK_GROUP_ID")


def get_wall_upload_url():
    url = "https://api.vk.com/method/photos.getWallUploadServer"
    params = {
        "group_id": vk_group_id,
        "access_token": {vk_token},
        "v": 5.131
    }
    response = requests.get(url, params)
    response.raise_for_status()
    upload_url = response.json()["response"].get("upload_url")
    return upload_url


def get_save_params(upload_url, file):
    with open(file, "rb") as photo:
        photos = {
            "photo": photo,
        }
        response = requests.post(upload_url, files=photos)
    response.raise_for_status()
    save_params = response.json()
    os.remove(file)
    return save_params["photo"], save_params["hash"], save_params["server"]


def get_post_params(photo, hash, server):
    url = "https://api.vk.com/method/photos.saveWallPhoto"
    params = {
        "group_id": vk_group_id,
        "access_token": vk_token,
        "v": 5.131,
        "photo": photo,
        "hash": hash,
        "server": server,
    }
    response = requests.post(url, params=params)
    response.raise_for_status()
    save_response = response.json().get("response")[0]
    return save_response["id"], save_response["owner_id"]


def post_photo(file, message):
    upload_url = get_wall_upload_url()
    photo, hash, server = get_save_params(upload_url, file)
    media_id, owner_id = get_post_params(photo, hash, server)
    url = "https://api.vk.com/method/wall.post"
    params = {
        "owner_id": -vk_group_id,
        "access_token": vk_token,
        "v": 5.131,
        "from_group": 1,
        "attachments": f"photo{owner_id}_{media_id}",
        "message": message,
    }
    requests.post(url, params=params)
