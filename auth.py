from urls import AUTH
from dotenv import load_dotenv
import requests
import json
import os

load_dotenv()

USER = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')


def auth():
    base_url = AUTH
    return json.loads(requests.post(base_url, json={"n8fzs": USER, "p4dc22": PASSWORD}).text)

def cookie(cookie=auth()):
    cookie = cookie['end'].replace('/oauth?_f_id', ';_id')
    cookie = cookie.replace('&_s_id', ';_oid')
    cookie = cookie.replace('&_FSID', ';_ss')
    cookie = cookie.replace('&_SSID', ';_tty')
    return cookie
