import re
import orodja

def najdi_prvo(vzorec, niz):
    vsi = re.findall(vzorec, niz, flags = re.DOTALL)
    if vsi:
        return vsi[0]

def prestej(vzorec, niz):
    return len(re.findall(vzorec, niz, flags = re.DOTALL))

def izbrisi(vzorci, niz):
    for vzorec in vzorci:
        niz = re.sub(vzorec, "", niz, flags = re.DOTALL)
    return niz

def koren(url):
    return najdi_prvo("wikipedia.org/wiki/(.+)$", url)

def id(url):
    return najdi_prvo("www.wikidata.org/entity/Q(\d+)$", url)

def datum(niz):
    if niz:
        if "-" in niz:
            return tuple([int(st) for st in najdi_prvo("(^.+)T", niz).split("-")])

def st_besed(url, vzorec):
    html = orodja.preberi_stran(url)
    if html:
        besedilo = najdi_prvo(vzorec, html)
        if besedilo:
            besedilo = izbrisi(["(<.*?>)", "^(\s+?)\S", "\S(\s+?)$", ""], besedilo)
            return prestej("\S(\s+?)\S", besedilo) + 1

def st_povezav(url):
    html = orodja.preberi_stran(url)
    if html:
        return prestej("<li><a href", html)

def st_ogledov(url):
    html = orodja.preberi_stran(url)
    if html:
        ogledi = najdi_prvo('</td><td><div class="mw-pvi-month">(\d+?,?\.?\d*?)</div>', html)
        if ogledi:
            return int(ogledi.replace(",", "").replace(".", ""))

def povezave_slo(koren):
    return st_povezav("https://sl.wikipedia.org/w/index.php?title=Posebno:KajSePovezujeSem/" + koren + "&limit=5000")

def povezave_ang(koren):
    return st_povezav("https://en.wikipedia.org/w/index.php?title=Special:WhatLinksHere/" + koren + "&limit=5000")

def ogledi_slo(koren):
    return st_ogledov("https://sl.wikipedia.org/w/index.php?title=" + koren + "&action=info")

def ogledi_ang(koren):
    return st_ogledov("https://en.wikipedia.org/w/index.php?title=" + koren + "&action=info")

def dolzina_slo(koren):
    return st_besed("https://sl.wikipedia.org/wiki/" + koren, '<div id="siteSub" class="noprint">Iz Wikipedije, proste enciklopedije</div>(.*?)</div><noscript><img src=')
    
def dolzina_ang(koren):
    return st_besed("https://en.wikipedia.org/wiki/" + koren, '<div id="siteSub" class="noprint">From Wikipedia, the free encyclopedia</div>(.*?)</div><noscript><img src=')