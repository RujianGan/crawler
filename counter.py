import pymongo
from page_prasing import item_urls, shouji_urls, shouji_info
import time


while True:
    print(shouji_info.find().count())
    time.sleep(5)
