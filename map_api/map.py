import os
from dotenv import load_dotenv
import requests

load_dotenv()

sk_map_key = os.getenv("SK_MAP_KEY")

def get_routes_by_coordinates(startX, startY, endX, endY):
    map_url = "https://apis.openapi.sk.com/tmap/routes/pedestrian?version=1&callback=function"
    payload = {
    "startX": startX,
    "startY": startY,
    "angle": 90,
    "speed": 30,
    "endPoiId": "10001",
    "endX": endX,
    "endY": endY,
    "passList": "126.92774822,37.55395475_126.92577620,37.55337145",
    "reqCoordType": "WGS84GEO",
    "startName": "%EC%B6%9C%EB%B0%9C",
    "endName": "%EB%8F%84%EC%B0%A9",
    "searchOption": "0",
    "resCoordType": "WGS84GEO",
    "sort": "index"
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "appKey": sk_map_key
    }
    response = requests.post(map_url, json=payload, headers=headers)
    return response.json()


def coordinates_by_address(address):
    url = f"https://apis.openapi.sk.com/tmap/geo/postcode?version=1&callback=function&addr={address}addressFlag=F01&coordType=WGS84GEO&format=json&page=1&count=20"
    headers = {
    "accept": "application/json",
    "appKey": sk_map_key
    }

    response = requests.get(url, headers=headers)



