#!/usr/bin/env python
# -*- coding:utf-8 -*-

def findnum(lst:list,sum:int):
    """

    给定一个整型列表，请实现从其中找出2个数的和为某一个指定的值
    如：lst =[1,5,2,7,4,9]，指定的目标值为11，可以从中找出 2和9之和为11 
    """

    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            if lst[i] + lst[j] == sum:
                print('列表{}中{}与{}的和为{}'.format(lst,lst[i],lst[j],sum))



findnum([1,5,2,7,4,9],11)
