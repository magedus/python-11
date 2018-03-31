#!/bin/env python
# -*- coding:utf-8 -*-

#导入模块
import random,string


lst = []
length = 0
while length < 10 :
    #生成随机数
    number = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    
    #如果生成的数不在列表中就追加进去
    if number not in lst:
        lst.append(number)
        length += 1
    print(number)
