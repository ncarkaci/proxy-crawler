# source : https://github.com/kursion/security-proxy-crawler/blob/master/crawler.py
# author : Yves Lange

import urllib2
import re


# Simply returns the html page from nntime.com
def getHTML(page):
    page = str(page).zfill(2)
    url = "http://nntime.com/proxy-updated-{:}.htm".format(page)

    print('Crawling url : '+url)
    req = urllib2.Request(url)
    return urllib2.urlopen(req).read()


# Hack JavaScript codes of nntime.com to parse the port number.
# They replaced the port number by `document.write(":"+r+i)`
# where 'r' and 'i' should be the port number. This function
# returns a dict with the corresponding letter as key and number
# as values.
def getHackCodes(htmlPage):
    codes = {}
    parseCode = r"((?:[a-z]=[0-9];)+)"
    matchesCode = re.findall(parseCode, htmlPage)
    for code in matchesCode[0].split(";")[:-1]:
        v = code.split("=")
        codes[v[0]] = v[1]
    return codes


# Decode the row to have the proxy IP:PORT
# This will replace the encoded letter by the numbers from codes.
def decodeRow(codes, row):
    m = re.findall(r'((?:[0-9]{1,3}\.){3}[0-9]{1,3})', row)
    if len(m) == 0:
        return None
    ip = m[0]

    pEnc = re.findall(r'document\.write\(":"((?:\+[a-z]){0,4})', row)
    portTmp = []
    if len(pEnc) > 0:
        pDec = pEnc[0].split("+")[1:]
        for c in pDec:
            portTmp.append(codes[c])
    else:
        return None
    port = "".join(portTmp)
    return ip+":"+port


# Get proxies from nntime.com
def getProxies(startPage=1, endPage=13):

    proxies = []

    for page in range(startPage, endPage):

        htmlPage = getHTML(page)

        parseTable = r"<td>(.*?)</td>"
        matchesRow = re.findall(parseTable, htmlPage)

        codes = getHackCodes(htmlPage)

        for row in matchesRow:
            proxy = decodeRow(codes, row)
            if proxy is not None:
                # console.warn(proxy)
                proxies.append(proxy)

    return proxies
