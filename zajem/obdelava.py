import orodja
import wiki_zajem as wiki
import poizvedba
import os
import datetime

if orodja.ne_obstaja(poizvedba.path_json):
    poizvedba.zapisi_json(poizvedba.path_json, poizvedba.dat_rq)
    pass

zacasni_json = os.path.join("..", "podatki", "json_zacasni.json")
novi_json = os.path.join("..", "podatki", "json_obdelan.json")
neslovenski_koreni = [" von ", "W", "pp"]
spol = {"moški": "Moški", "ženski": "Ženska"}

def slovensko_ime(ime):
    return all([koren not in ime for koren in neslovenski_koreni])

def starost(rojstvo, smrt, smrt_type):
    if smrt_type == "bnode":
        return
    elif not smrt:
        smrt = tuple([int(st) for st in str(datetime.date.today()).split("-")])
    return smrt[0] - rojstvo[0] - int(rojstvo[1:] > smrt[1:])

def wiki_slovar(koren_slo, koren_ang):
    return {
        "Ogledi Slo": wiki.ogledi_slo(koren_slo),
        "Ogledi Ang": wiki.ogledi_ang(koren_ang),
        "Povezave Slo": wiki.povezave_slo(koren_slo),
        "Povezave Ang": wiki.povezave_ang(koren_ang),
        "Dolzina Slo": wiki.dolzina_slo(koren_slo),
        "Dolzina Ang": wiki.dolzina_ang(koren_ang)
    }

def predelaj_slovar(slovar):
    predelan = {
        "ID" : int(wiki.id(slovar["id"]["value"])),
        "Ime": slovar["ime"]["value"],
        "Spol": spol.get(slovar["spol"]["value"], None),
        "Rojstni Kraj": slovar.get("kraj", {}).get("value", None),
        "Poklici": [poklic.capitalize() for poklic in slovar["poklici"]["value"].split(";")]
    }
    rojstvo = wiki.datum(slovar["rojstvo"]["value"])
    smrt = wiki.datum(slovar.get("smrt", {}).get("value", None))
    predelan["Leto Rojstva"] = rojstvo[0]
    predelan["Starost"] = starost(rojstvo, smrt, slovar.get("smrt", {}).get("type", None))
    predelan["Mrtev"] = bool(smrt)
    koren_slo = wiki.koren(slovar["WikiSlo"]["value"])
    koren_ang = wiki.koren(slovar["WikiAng"]["value"])
    predelan.update(wiki_slovar(koren_slo, koren_ang))
    return predelan

def obdelaj_json():
    neobdelani = orodja.nalozi_json(poizvedba.path_json)
    if orodja.ne_obstaja(zacasni_json):
        obdelani = {}
    else:
        obdelani = orodja.nalozi_json(zacasni_json)
    for slovar_podatkov in neobdelani:
        id_osebe = wiki.id(slovar_podatkov["id"]["value"])
        if id_osebe in obdelani or not slovensko_ime(slovar_podatkov["ime"]["value"]):
            continue
        else:
            obdelani[id_osebe] = predelaj_slovar(slovar_podatkov)
            print("Obdelani podatki za: {}.".format(slovar_podatkov["ime"]["value"]))
            orodja.zapisi_json(zacasni_json, obdelani)
    seznam_vseh = list(obdelani.values())
    seznam_vseh.sort(key = lambda po: po["ID"])
    orodja.zapisi_json(novi_json, seznam_vseh)
    print("Končano")