# 1、问题描述：一个5位数，判断它是不是回文数。


def is_palindromic(num: int):
    s1 = str(num)
    s2 = s1[::-1]
    # reversed  abc->cba  aba -> aba
    if s1 == s2:
        return '{} 是回文数'.format(num)
    return '{} 不是回文数'.format(num)


def is_palindromic_2(num: int):
    s1 = str(num)
    length = len(s1)
    # 12331
    for i in range(length // 2):
        if s1[i] != s1[length - i - 1]:
            return '{} 不是回文数'.format(num)
    return '{} 是回文数'.format(num)


# 2、随机生成20个数字，并且筛选出其中最大的3个数
import string
import random


def gen_random_num(nums):
    s1 = string.digits
    lst = []
    for i in range(nums):
        num = int(''.join(random.sample(s1, 5)))
        lst.append(num)
    lst.reverse()
    return lst[-3:]


a = '1111222'
b = a[::-1]
print(b, a)


def test():
    abc = 1
    def wrap():
        print('wrap....')
        return abc
    return wrap


def test2(f):
    def wrap(*args, **kwargs):
        print('f execute ...')
        return f(*args, **kwargs)
    return wrap

@test2
def print_hello():
    print('hello ...')
    return 'hello world'

@test2
def print_hi():
    print('hi .....')
    return 'hi world'

import time

def test(f):
    def wrap(*args, **kwargs):
        start_time = time.time()
        ret = f(*args, **kwargs)
        end_time = time.time()
        print('\n', 'use time ', end_time-start_time)
        return ret
    return wrap

@test
def test1(*args, **kwargs):
    time.sleep(1)
    for i in range(1, 10):
        for j in range(1, i+1):
            print('{}*{}={}'.format(j, i, i*j), end="\t")
    return 'abc'
ret1 = test1()
print(ret1)


def decorator(func):
    def _deco(*args, **kwargs):
        begin = time.time()
        ret = func(*args, **kwargs)
        end = time.time()
        print(end-begin)
        return ret
    return _deco



def test4(timeout):
    print(timeout, '------', id(timeout))
    def test3(f):
        print(f, '====')
        def wrap(*args, **kwargs):
            start_time = time.time()
            ret = f(*args, **kwargs)
            end_time = time.time()
            use_time = end_time - start_time
            if timeout < use_time:
                print('\n', 'use time ', use_time)
            return ret

        return wrap
    return test3

@test4(10)
def print_aa(name):
    time.sleep(1.5)
    print(name)

f3 = test4(10)(print_aa)
def abc():
    print('sasas')

print(print_aa.__closure__)