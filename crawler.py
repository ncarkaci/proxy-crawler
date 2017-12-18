from proxies import nordvpnCrawler, nntimecomCrawler, premproxycomCrawler, cnproxyCrawler, waselproxyCrawler


def addProxyList(proxies):

    with open('proxy_list.txt','r') as input_file:

        proxy_list = input_file.read().split('\n')
        print(str(len(proxy_list)))

    proxy_list = proxy_list+proxies
    proxy_list = list(set(proxy_list))

    with open('proxy_list.txt', 'a') as output_file:
        output_file.writelines(["%s\n" % proxy_address for proxy_address in proxy_list])


# https://nordvpn.com
addProxyList(nordvpnCrawler.getProxies(limit=500000))

# https://premproxy.com
addProxyList(premproxycomCrawler.getProxies())

# http://nntime.com
addProxyList(nntimecomCrawler.getProxies())

# http://www.cnproxy.com
addProxyList(cnproxyCrawler.getProxies())

# Crawle http://www2.waselproxy.com/
addProxyList(waselproxyCrawler.getProxies())


