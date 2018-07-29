import requests
import threading


# 1、并发抓取10 个url，并且打印出它们的状态码、和文本内容

def fetch(urls: list):
    def req(url):
        ret = requests.get(url)
        print(ret.status_code, ret.text)

    for l in urls:
        threading.Thread(target=req, args=(l,))


# 2、上下文管理是什么？请实现一个python 类，具有上下文管理功能

class A:
    def __init__(self, name):
        self.name = name
        print('__init__')

    def __enter__(self):
        print('__enter__', self.name)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('__exit__')


with A('ba') as a:
    print('hello', a)

with A('a'):
    print('hi')
