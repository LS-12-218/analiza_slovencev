Analiza podatkov o znanih Slovencev
===================================

Pirdobil in aniliziral bom podatke o Slovencih, ki so dovolj znani, da imajo Wipidedijin članek v slovenščini in angleščini. Uporabil bom orodje za poizvedbo na strani Wikidata: https://query.wikidata.org/#SELECT%20%3Foseba%20%3FosebaLabel%0AWHERE%0A%7B%0A%09%3Foseba%20wdt%3AP31%20wd%3AQ5.%0A%20%20%20%20%3Foseba%20wdt%3AP27%20wd%3AQ215.%0A%09FILTER%20EXISTS%20%7B%20%3Fwslo%20schema%3Aabout%20%3Foseba%20.%20%3Fwslo%20schema%3AisPartOf%20%3Chttps%3A%2F%2Fsl.wikipedia.org%2F%3E%20%7D%0A%09FILTER%20EXISTS%20%7B%20%3Fwang%20schema%3Aabout%20%3Foseba%20.%20%3Fwang%20schema%3AisPartOf%20%3Chttps%3A%2F%2Fen.wikipedia.org%2F%3E%20%7D%0A%09SERVICE%20wikibase%3Alabel%20%7B%0A%09%09bd%3AserviceParam%20wikibase%3Alanguage%20%22sl%2Cen%22%20.%0A%09%7D%0A%7D


#### Podatki, ki jih bom pridobil:
* Ime in spol osebe
* Letnica rojstva in smrti
* Rojstni kraj
* Poklic oziroma področje delovanja
* Velikost članka o osebi na slovenski in angleški Wikipediji
* Število ogledov članka v zadnjih 30 dneh
* Število povezav na članek

#### Hipoteze:
* Kateri Slovenci so najbloj znani doma in kateri v tujini?
* Kateri so najpogostejši poklici?
* Ali je življenska doba odvisna od poklica?
* V kakšni zvezi so dolžina članka, število ogledov in število povezav?
* V katerih krajih se je rodilo največ znanih Slovencev?
