import requests
from bs4 import BeautifulSoup
import pymongo
import random
from ip import proxy_ips


client = pymongo.MongoClient('localhost', 27017)
tongcheng = client['tongcheng']
item_urls = tongcheng['item_urls']
item_info = tongcheng['item_info']
shouji_urls = tongcheng['shouji_urls']
shouji_info = tongcheng['shouji_info']


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
    'Connection': 'keep-alive'
}

proxy_ip = random.choice(proxy_ips.split()) # 随机获取代理ip
proxies = {'http': proxy_ip}


def get_item_urls(channel, page, who_sells=0):

    url = '{}{}/pn{}/'.format(channel, who_sells, page)
    try:
        wb_data = requests.get(url, headers=headers, proxies=proxies)
        soup = BeautifulSoup(wb_data.text, 'lxml')
    except Exception as e:
        print(e)
        return 0

    # judge the page has url or not
    if soup.find('td', 't'):
        for link in soup.select('td.t > a'):
            item_url = link.get('href')
            if item_url.find('target') > -1:
                continue
            item_url = item_url.split('?')[0]
            shouji_urls.insert_one({'url': item_url})
            print(item_url)
    else:
        pass


def get_item_info(url):
    try:
        wb_data = requests.get(url, headers=headers, proxies=proxies)
        soup = BeautifulSoup(wb_data.text, 'lxml')
    except Exception as e:
        print(e)
        return 0

    if soup.find('span', 'soldout_btn'):
        print('soldout')
        pass
    else:
        data = {
            'title': soup.select('h1.info_titile')[0].text,
            'price': soup.select('span.price_now > i')[0].text,
            'area' : soup.select('div.palce_li > span > i')[0].text,
            'describe': soup.select('div.baby_kuang.clearfix > p')[0].text,
            'image': soup.select('#img1')[0].get('rel'),
            'url'  : url
        }
        shouji_info.insert_one(data)
        print(data['title'])
