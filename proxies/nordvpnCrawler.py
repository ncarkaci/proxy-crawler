import requests
from bs4 import BeautifulSoup
import json


# Get proxies from https://www.hide-my-ip.com/proxylist.shtml
def getProxies(type=['http','https'],limit=10000,startPage=0, endPage=50):
    ip_type_convert = {'HTTP': 'http', 'HTTPS': 'https'}

    proxies = []

    ip_type_convert = {'HTTP': 'http', 'HTTPS': 'https'}
    for page in range(startPage, endPage, 25):
        try:
            url = "https://nordvpn.com/wp-admin/admin-ajax.php?searchParameters[0][name]=proxy-country" \
                      "&searchParameters[0][value]=" \
                      "&searchParameters[1][name]=proxy-ports" \
                      "&searchParameters[1][value]=" \
                      "&offset=" + str(page) + "" \
                      "&limit="+str(limit)+"" \
                      "&action=getProxies"

            print('Crawling url : ' + url)

            response = requests.get(url)
            response_json = response.json()
            for i in range(len(response_json)):
                ip_type = (response_json[i]['type']).encode('utf-8')

                if ip_type not in type:
                    continue
                ip_port = (response_json[i]['port']).encode('utf-8')
                ip_ip = (response_json[i]['ip']).encode('utf-8')
                # ip = ip_type_convert[ip_type] + "://" + ip_ip + ":" + ip_port
                ip = ip_ip + ":" + ip_port # No http title
                proxies.append(ip)
        except:
            continue

    return proxies

print(getProxies())
