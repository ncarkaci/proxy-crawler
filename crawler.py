from proxies import nordvpnCrawler, nntimecomCrawler, premproxycomCrawler, cnproxyCrawler, waselproxyCrawler


def addProxyList(proxies):

    with open('proxy_list.txt','r') as input_file:

        proxy_list = input_file.read().split('\n')
        print(str(len(proxy_list)))

    proxy_list = proxy_list+proxies
    proxy_list = list(set(proxy_list))

    with open('proxy_list.txt', 'a') as output_file:
        output_file.writelines(["%s\n" % proxy_address for proxy_address in proxy_list])

addProxyList(nordvpnCrawler.getProxies(type=['HTTPS'], limit=500000))
addProxyList(premproxycomCrawler.getProxies())
addProxyList(nntimecomCrawler.getProxies())
addProxyList(cnproxyCrawler.getProxies())
addProxyList(waselproxyCrawler.getProxies())


