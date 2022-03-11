from bs4 import BeautifulSoup
from simplejson import load
from urls import BUSINESS
import requests
import auth
import os

def business():
    business = requests.get(BUSINESS, headers={"Cookie": "test=cookies_are_working_properly;"+auth.cookie()})
    page = BeautifulSoup(business._content, 'lxml')
    links = page.find("ul", {"class": "urls"})
    links = links.find_all("li")

    business = {}

    for li in links:
        a = li.find("a")
        business.update({f"{a.text}": {"name": f"{a.text}", "link": f"{a.attrs['href']}"}})

    return business
