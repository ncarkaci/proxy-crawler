
import requests
from bs4 import BeautifulSoup

# Get proxies from http://www2.waselproxy.com/
def getProxies(startPage=1, endPage=74):

    proxies = []

    for page in range(startPage, endPage):

        try:
            url = "http://www2.waselproxy.com/page/" + str(page)
            print('Crawling url : ' + url)
            response = requests.get(url)
            soup = BeautifulSoup(response.content, "lxml")
            rows = soup.find_all("td")

            ip_index = 0
            port_index = 1

            while(ip_index < len(rows)):

                proxy = rows[ip_index].text+':'+rows[port_index].text
                ip_index += 4
                port_index += 4

                proxies.append(proxy)
        except:
            continue

    return proxies
