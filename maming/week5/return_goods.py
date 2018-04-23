# coding: utf-8
import random

def random_index(rate):
    start = 0
    randnum = random.randint(1, sum(rate))
    for index, item in enumerate(rate):
        start += item
        if randnum <= start:
            break
    return index

def get_count():
    arr = ('袜子', '鞋子', '拖鞋', '项链')
    rate = (10, 20, 30,40)

    socks_times = 0
    shoes_times = 0
    slippers_times = 0
    nickle_times=0
    for _  in range(100):
        if arr[random_index(rate)] == '袜子':
            socks_times += 1
        if arr[random_index(rate)] == '鞋子':
            shoes_times += 1
        if arr[random_index(rate)] == '拖鞋':
            slippers_times += 1
        if arr[random_index(rate)] == '项链':
            nickle_times +=1

    return  (socks_times, shoes_times, slippers_times ,nickle_times)

if __name__ == '__main__':
    print(get_count())
