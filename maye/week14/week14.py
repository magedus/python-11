 1、并发抓取10 个url，并且打印出它们的状态码、和文本内容
# # 2、上下文管理是什么？请实现一个python 类，具有上下文管理功能

import requests
from lxml import etree
import logging
import time
import random
import threading

logging.basicConfig(level=logging.INFO)

name, score, comment = [], [], []

def danye_crawl(page):
    time.sleep(random.uniform(4, 6))
    url = 'https://movie.douban.com/subject/6390825/comments?start=%s&limit=20&sort=new_score&status=P&percent_type='%(page*20)
    response = requests.get(url)
    response = etree.HTML(response.content.decode('utf-8'))
    logging.info(requests.get(url).status_code)
    for i in range(1,21):
        comment_list = response.xpath('//*[@id="comments"]/div[%s]/div[2]/p'%(i))
        logging.info(comment_list[0].text)

for i in range(11):
    t = threading.Thread(target=danye_crawl,args=(0,))
    t.start()




# class Open:
#     def __init__(self,path):
#         self.path = path
#         self.file = open(self.path)
#
#     def __enter__(self):
#         return self.file.read()
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         return self.file.close()
#
# with Open('/Users/mac/Desktop/word.txt') as f:
#     for line in f:
#         print(f)

