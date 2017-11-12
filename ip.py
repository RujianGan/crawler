# http://www.xicidaili.com/nn/

import requests
from bs4 import BeautifulSoup


ip_url = 'http://www.xicidaili.com/nn/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
    'Connection': 'keep-alive'
}


def get_ip_list(url):

    wb_data = requests.get(url, headers=headers)
    soup = BeautifulSoup(wb_data.text, 'lxml')

    ips = soup.select('tr.odd > td:nth-of-type(2)')
    ports = soup.select('tr.odd > td:nth-of-type(3)')

    for ip, port in zip(ips, ports):
        agency_ip = (ip.text + ':' + port.text)
        print(agency_ip)


# get_ip_list(ip_url)
# 挑刚更新的

proxy_ips = '''
120.27.131.204:3128
61.135.217.7:80
118.114.77.47:8080
'''