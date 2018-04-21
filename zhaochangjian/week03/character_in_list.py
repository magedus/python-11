#-*- coding: utf-8 -*-
# 1、给出任意一个列表，请查找出x元素是否在列表里面，如果存在返回1，不存在返回0

a_list = list(range(20))

def finder(x):
    if x in a_list:
        return 1
    else:
        return 0
        
        
print(finder(10))
print(finder(24))
