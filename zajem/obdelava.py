import orodja
import wiki_zajem as wiki
import poizvedba
import os
import datetime


zacasni_json = os.path.join("..", "podatki", "json_zacasni.json")
novi_json = os.path.join("..", "podatki", "json_obdelan.json")
podatki_csv = os.path.join("..", "podatki", "csv_podatki.csv")
poklici_csv = os.path.join("..", "podatki", "csv_poklici.csv")
neslovenski_koreni = [" von ", "W", "pp", "orio", "Ražnatović", "Inzko"]
spol = {"moški": "Moški", "ženski": "Ženska"}

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
        "Dolžina Slo": wiki.dolzina_slo(koren_slo),
        "Dolžina Ang": wiki.dolzina_ang(koren_ang)
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

def slovensko_ime(ime):
    return all([koren not in ime for koren in neslovenski_koreni])

def filtriraj(slovar_podatkov):
    star = slovar_podatkov["Starost"]
    if not star:
        slovar_podatkov["Mrtev"] = True
    else:
        if star > 90:
            if not slovar_podatkov["Mrtev"] and slovar_podatkov.get("Ogledi Ang", 0) <= 40 or slovar_podatkov["Leto Rojstva"] <= 1700:
                slovar_podatkov["Starost"] = None
    return slovar_podatkov

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
            orodja.zapisi_json(zacasni_json, obdelani)
            print("Obdelani podatki za: {} ({}%)".format(slovar_podatkov["ime"]["value"], len(obdelani) * 100 // len(neobdelani)))

    seznam_vseh = [filtriraj(podatek) for podatek in obdelani.values() if slovensko_ime(podatek["Ime"])]
    seznam_vseh.sort(key = lambda podatek: podatek["ID"])
    orodja.zapisi_json(novi_json, seznam_vseh)
    print("Končano")

def main():
    if orodja.ne_obstaja(poizvedba.path_json):
        poizvedba.zapisi_json(poizvedba.path_json, poizvedba.dat_rq)
    obdelaj_json()
    podatki = orodja.nalozi_json(novi_json)
    poklici = [{"ID": podatek["ID"], "Poklic": poklic} for podatek in podatki for poklic in podatek.pop("Poklici")]
    orodja.zapisi_csv(podatki_csv, podatki)
    orodja.zapisi_csv(poklici_csv, poklici)

if __name__ == "__main__":
    main()