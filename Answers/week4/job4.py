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
    for i in range(length//2):
        if s1[i] != s1[length-i-1]:
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