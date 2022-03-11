from bs4 import BeautifulSoup
from urls import BASE
import auth
import requests

def reports(business):
    reports = BeautifulSoup(requests.get(BASE+business["link"], headers={"Cookie": "test=cookies_are_working_properly;"+auth.cookie()})._content)

    cnpj = reports.find("h3", {"id": "empresa"}).text
    cnpj = cnpj.replace(".", "")
    cnpj = cnpj.replace("/", "")
    cnpj = cnpj.replace("-", "")
    ul = reports.find("ul")
    li = ul.find_all("li")

    reports = {}

    for content in li:
        a = content.find("a")
        reports.update(
            {f"{a.text}": {"cnpj": f"{cnpj}", "link": f"{a.attrs['href']}"}})

    return reports

