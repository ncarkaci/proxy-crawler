import requests
import json


# Get proxies from https://www.hide-my-ip.com/proxylist.shtml
def getProxies(limit=10000,startPage=0, endPage=50):

    proxies = []

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

            response_json = requests.get(url).json()

            for response in response_json:

                ip_port = str(response['port']).encode('utf-8').decode()
                ip_ip = str(response['ip']).encode('utf-8').decode()
                ip = ip_ip + ":" + ip_port # No http title
                proxies.append(ip)
        except Exception as err:
            print(err)
            continue

    return proxies

