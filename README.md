Analiza podatkov o znanih Slovencev
===================================

Pirdobil in aniliziral bom podatke o Slovencih, ki so dovolj znani, da imajo Wipidedijin članek v slovenščini in angleščini. Uporabil bom orodje za poizvedbo na strani Wikidata:
[https://query.wikidata.org/](https://query.wikidata.org/#SELECT%20%0A%3Fid%20%28SAMPLE%28%3Fime%29%20AS%20%3Fime%29%20%28SAMPLE%28%3Fspol_ime%29%20as%20%3Fspol%29%0A%28SAMPLE%28%3Frojstvo%29%20AS%20%3Frojstvo%29%20%28SAMPLE%28%3Fsmrt%29%20AS%20%3Fsmrt%29%20%28SAMPLE%28%3Fkraj_ime%29%20as%20%3Fkraj%29%0A%28GROUP_CONCAT%28DISTINCT%20%3Fpoklic_ime%3B%20SEPARATOR%3D%22%3B%22%29%20AS%20%3Fpoklici%29%0A%28SAMPLE%28%3FWikiSlo%29%20AS%20%3FWikiSlo%29%20%28SAMPLE%28%3FWikiAng%29%20AS%20%3FWikiAng%29%0A%0AWHERE%20%7B%0A%20%20%3Fid%20wdt%3AP31%20wd%3AQ5%3B%0A%20%20%20%20%20%20wdt%3AP21%20%3Fspol%3B%0A%20%20%20%20%20%20wdt%3AP106%20%3Fpoklic%3B%0A%20%20%20%20%20%20wdt%3AP569%20%3Frojstvo.%0A%20%20%7B%0A%20%20%20%20%7B%3Fid%20wdt%3AP27%20wd%3AQ215.%7D%20%23ima%20slovensko%20dr%C5%BEavljanstvo%0A%20%20%20%20UNION%20%7B%3Fid%20wdt%3AP1412%20wd%3AQ9063.%7D%20%23je%20govoril%20slovensko%0A%20%20%20%20UNION%20%7B%3Fid%20wdt%3AP19%20%5Bwdt%3AP17%20wd%3AQ215%5D.%7D%20%23se%20je%20rodil%20v%20dana%C5%A1nji%20Sloveniji%0A%20%20%7D%0A%20%20OPTIONAL%20%7B%3Fid%20wdt%3AP570%20%3Fsmrt.%7D%0A%20%20OPTIONAL%20%7B%3Fid%20wdt%3AP19%20%3Fkraj.%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%7B%3Fkraj%20wdt%3AP31%20wd%3AQ515%7D%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20UNION%20%7B%3Fkraj%20wdt%3AP31%20wd%3AQ3957%7D%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20UNION%20%7B%3Fkraj%20wdt%3AP31%20wd%3AQ486972%7D%20%23je%20mesto%2C%20naselje%20ali%20vas%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%20%20%20%20%20%7D%0A%20%20%3FWikiSlo%20schema%3Aabout%20%3Fid.%0A%20%20%3FWikiSlo%20schema%3AisPartOf%20%3Chttps%3A%2F%2Fsl.wikipedia.org%2F%3E.%20%23slovenska%20wiki%20stran%0A%20%20%3FWikiAng%20schema%3Aabout%20%3Fid.%0A%20%20%3FWikiAng%20schema%3AisPartOf%20%3Chttps%3A%2F%2Fen.wikipedia.org%2F%3E.%20%23angle%C5%A1ka%20wiki%20stran%0A%20%20SERVICE%20wikibase%3Alabel%20%7B%20%0A%20%20%20%20bd%3AserviceParam%20wikibase%3Alanguage%20%22sl%2C%20en%22.%20%23dobi%20imena%20objektov%0A%20%20%20%20%3Fid%20rdfs%3Alabel%20%3Fime.%0A%20%20%20%20%3Fspol%20rdfs%3Alabel%20%3Fspol_ime.%0A%20%20%20%20%3Fkraj%20rdfs%3Alabel%20%3Fkraj_ime.%0A%20%20%20%20%3Fpoklic%20rdfs%3Alabel%20%3Fpoklic_ime.%0A%20%20%7D%0A%20%20FILTER%28LANG%28%3Fpoklic_ime%29%20%3D%20%22sl%22%29%20%23le%20poklici%2C%20za%20katere%20obstajajo%20slovenska%20imena%0A%20%20FILTER%28LANG%28%3Fime%29%20%3D%20%22sl%22%29%0A%20%20FILTER%28%3Frojstvo%20%3E%3D%20%221000-01-01T00%3A00%3A00Z%22%5E%5Exsd%3AdateTime%29%0A%7D%0AGROUP%20BY%20%3Fid)

## Podatki
##### CSV
V datoteki _podatki.csv_ so shranjeni vsi zajeti podatki o osebi razen poklicev.  
V datoteki _poklici.csv_ so shranjeni poklici z ID-jem osebe.
##### Python skripte in JSON
Poizvedba.py zahteva poizvedbo in shrani podatke v json_neobdelan.json.  
Obdelava.py in wiki_zajem.py zajameta ustrezne Wikipedia strani in obdelata podatke, ki se shranjujejo v pomožni datoteki json_zacasni.json in json_obdelan.json.

#### Podatki, ki jih bom pridobil:
* Ime in spol osebe
* Letnica rojstva in smrti
* Rojstni kraj
* Poklic oziroma področje delovanja
* Velikost članka o osebi na slovenski in angleški Wikipediji
* Število ogledov članka v zadnjih 30 dneh
* Število povezav na članek z drugih wiki strani

#### Hipoteze:
* Kateri Slovenci so najbloj znani doma in kateri v tujini?
* Kakšno je razmerje med spoloma in kako se je spreminjalo skozi čas?
* Kateri so najpogostejši poklici?
* Kako je življenska doba odvisna od leta rojstva, poklica in spola?
* V kakšni zvezi so dolžina članka, število ogledov in število povezav?
* V katerih krajih se je rodilo največ znanih Slovencev?