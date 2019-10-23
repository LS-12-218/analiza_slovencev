import os
import json
import csv
import re
import requests

def ne_obstaja(datoteka):
    if datoteka:
        return not os.path.exists(datoteka)

def ustvari_mape(datoteka):
    pot = os.path.dirname(datoteka)
    if ne_obstaja(pot):
        os.makedirs(pot, exist_ok = True)

def preberi(datoteka):
    with open(datoteka, encoding = "utf-8") as dat:
        return dat.read()

def zapisi_json(datoteka, objekt, zamik = 2):
    ustvari_mape(datoteka)
    with open(datoteka, "w", encoding = "utf-8") as dat:
        json.dump(objekt, dat, indent = zamik, ensure_ascii = False)

def nalozi_json(datoteka):
    with open(datoteka, encoding = "utf-8") as dat:
        return json.load(dat)

def preberi_stran(url):
    try:
        html = requests.get(url)
        html.encoding = "utf-8"
        html = html.text
    except:
        print("Napaka")
        return
    return html