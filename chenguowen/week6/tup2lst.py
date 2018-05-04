#/usr/bin/env python
# -*- coding: utf-8 -*-
# 将两元组生成一个列表

def tup2lst(arg1,arg2):
    '''
    使用两个元组中的元素，生成一个特定格式的列表
    
    (('a','b')), ((1,2)) --> [{'a':1},{'b':2}]
    '''
    
    return (lambda x,y:[{k:v} for k,v in zip(x,y)])(arg1,arg2)

tup1,tup2 = (('a'),('b')),(('c'),('d'))
print(tup2lst(tup1,tup2))
