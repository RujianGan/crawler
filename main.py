from channel_extracing import channel_links
from page_prasing import get_item_urls, get_item_info, item_urls, item_info, shouji_urls, shouji_info
from multiprocessing import Pool


# db_urls = [item['url'] for item in item_urls.find()]
# index_urls = [item['url'] for item in item_info.find()]


def get_all_item_urls(channel):
    for i in range(1, 100):
        get_item_urls(channel, i)


def get_all_item_info(urls):
    for url in urls.find():
        print(url['url'])
        get_item_info(url['url'])


# if __name__ == '__main__':
#     pool = Pool()
#     pool.map(get_all_item_urls, channel_links.split())
#     pool.close()
#     pool.join()
# get_all_item_urls('http://sh.58.com/shouji/')
get_all_item_info(item_urls)
