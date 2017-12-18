import urllib


# source : https://github.com/sempr/proxy-tools/blob/master/proxy-crawler.py
def handle(url):

    text = []
    for line in urllib.urlopen(url):
        if line.find("SCRIPT")>0:
            text.append(line.decode('gbk').strip())
    change = text[1]
    text = [x for x in text[2:] if x.find("HTTP")>0]

    changedict = dict([tuple(x.replace('\"','').split("=")) for x in change.split(';')][:-1])
    proxies = []
    for t in text:
        try:
            ta = [x.replace("</td>","") for x in t[4:-5].split('<td>') if x]
            idx0 = ta[0].find("\":\"+")
            idx1 = ta[0].find(")</SCRIPT>")
            idx2 = ta[0].find("<SCRIPT")
            port_orig = ta[0][idx0+4:idx1].replace("+","")
            port = ''.join([changedict[p] for p in port_orig])

            proxy = ta[0][:idx2]+':'+port
            proxies.append(proxy)
        except:
            continue
    return proxies


# Get proxies from premproxy.com
def getProxies(startPage=1, endPage=11):
    urls = ['http://www.cnproxy.com/proxy%d.html' % x for x in range(startPage, endPage)] + \
           ['http://www.cnproxy.com/proxyedu%d.html' % x for x in range(1, 3)]

    proxies = []
    for url in urls:
        try:
            print('Crawling url : ' + url)
            proxies = handle(url)
        except:
            continue

    return proxies