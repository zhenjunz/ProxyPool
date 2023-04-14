from proxypool.schemas.proxy import Proxy
from proxypool.crawlers.base import BaseCrawler
import re
import json
BASE_URL = 'https://raw.githubusercontent.com/HyperBeats/proxy-list/main/http.txt'


class HyperBeatsCrawler(BaseCrawler):
    """
    HyperBeats crawler,https://github.com/HyperBeats/proxy-list
    """
    urls = [BASE_URL]

    def parse(self, html):
        """
        parse html file to get proxies
        :return:
        """

        hosts_ports = html.split('\n')
        for addr in hosts_ports:
            if(addr):
                ip_address = addr.strip().split(':')
                host = ip_address[0]
                port = ip_address[1]
                yield Proxy(host=host, port=port)

if __name__ == '__main__':
    crawler = HyperBeatsCrawler()
    for proxy in crawler.crawl():
        print(proxy)
