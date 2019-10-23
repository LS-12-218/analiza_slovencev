import orodja
import wiki_zajem
import poizvedba
import os

if orodja.ne_obstaja(poizvedba.path_json):
    poizvedba.zapisi_json(poizvedba.path_json, poizvedba.dat_rq)

zacasni_json = os.path.join("..", "podatki", "json_zacasni.json")
novi_json = os.path.join("..", "podatki", "json_obdelan.json")
neslovenski_koreni = [" von ", "W", "pp"]

def slovensko_ime(ime):
    return all([koren not in ime for koren in neslovenski_koreni])