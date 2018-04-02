#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/3/31 上午10:33
__author__ = 'ZhanWei'
import random, string
def gencode(length):
    result = ''  # 创建空字符串
    s = string.ascii_letters+ string.digits  # 获取所有字母(大小写)和数字需导入string
    for n in range(length):
        str = s[random.randint(0, len(s) - 1)]  # 随机索引获得随机的字符
        result += str  # 字符拼接
    return result

def loop(length=10, count=200):
    for x in range(count):
        print (gencode(length))

loop(11, 6)  # 传入验证码长度和个数