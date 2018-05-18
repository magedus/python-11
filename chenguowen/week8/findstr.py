#!/usr/bin/env python
# -*- coding: utf-8 -*-


def findstr(str1:str,str2:str):
    """
    实现一个函数用于判断字符串str2是否是str1的子串。如果是，则该函数返回str2在str1中首次出 现的地址；否则，返回None。
    
    """
    
    if str2 in str1:
        print('{} 在 {} 出现的位置是：{}'.format(str2,str1,str1.index(str2)))
    else:
        return
    

findstr('Hello Python!','Python')
