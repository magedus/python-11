#2、给定一个整型列表，请实现从其中找出2个数的和为某一个指定的值？
import random

src_list = [1,5,2,7,4,9]

def find_num(src_list):
    src_set = set(src_list)
    while True:
        tmp = random.choice(src_list)
        if 11 - tmp in src_set:
            return 11 - tmp,tmp


print(find_num(src_list))

