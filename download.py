from dotenv import load_dotenv
from urls import BASE
import auth
import reports
import business
import requests
import json
import time
import os

load_dotenv()

USER = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')

def donwload():
    bns = business.business()

    for bn in bns:
        rps = reports.reports(bns[bn])

        for report in rps:
            ams = report.strip()
            csv = requests.post(
                BASE+"/athens/csv", json={"ams": ams, "cnpj": f"{rps[report]['cnpj']}"}, headers={"Cookie": "test=cookies_are_working_properly;"+auth.cookie()}).text

            try:
                csv = json.loads(csv)
            
                bn = bn.strip(" ")
                report = report.strip(" ")
                report = report.replace("#", "")
                report = report.replace("%", "")
                report = report.replace("*", "")
                report = report.replace(":", "")
                report = report.replace("<", "")
                report = report.replace(">", "")
                report = report.replace("?", "")
                report = report.replace("/", "")
                report = report.replace("|", "")


                try:
                    with open(f"./data/{bn}/{report}.csv", 'w', encoding="utf-8") as csvFile:
                        csvFile.write(csv['file'])
                except:
                    os.system(f'cd ./data && mkdir "{bn}"')
                    with open(f"./data/{bn}/{report}.csv", 'w', encoding="utf-8") as csvFile:
                        csvFile.write(csv['file'])

            except:
                print(f"Erro na empresa: {bn} Report: {report}")

            """ VAI TOMA NO CU TUPLA
            ....................../´¯/) 
            ....................,/¯../ 
            .................../..../ 
            ............./´¯/'...'/´¯¯`·¸ 
            ........../'/.../..../......./¨¯\ 
            ........('(...´...´.... ¯~/'...')      ┌∩┐(◣_◢)┌∩┐ DELETE THIS
            .........\.................'...../ 
            ..........''...\.......... _.·´ 
            ............\..............( 
            ..............\.............\...
            """

        time.sleep(30)

donwload()
