import orodja
import os
from SPARQLWrapper import SPARQLWrapper, JSON

path_json = os.path.join("..","podatki", "json_neobdelan.json")
dat_rq = "poizvedba.rq"

def rezultat(url, poizvedba):
    sparql = SPARQLWrapper(url)
    sparql.setQuery(poizvedba)
    sparql.setReturnFormat(JSON)
    vrnjen_slovar = sparql.query().convert()
    return vrnjen_slovar["results"]["bindings"]

def zapisi_json(dat_json, dat_sparqul):
    poizvedba = orodja.preberi(dat_rq)
    rezultati = rezultat("https://query.wikidata.org/sparql", poizvedba)
    orodja.zapisi_json(dat_json, rezultati)