
import urllib, re


# Get proxies from premproxy.com
def getProxies(startPage=1, endPage=13):

    proxies = []

    for page in range(startPage, endPage):

        try:

            page = str(page).zfill(2)
            url = "https://premproxy.com/list/ip-address-{:}.htm".format(page)
            print('Crawling url : ' + url)

            content = urllib.urlopen("http://www.samair.ru/proxy/ip-address-01.htm").read()

            matchesRow = re.findall('\d+\.\d+\.\d+\.\d+:\d+', content)

            for proxy in matchesRow:
                proxies.append(proxy)
        except:
            continue
    return proxies


