#!/usr/bin/env python
# -*- coding:utf-8 -*-
import random

def nums(x):
    global nums_lst
    nums_lst = [random.randrange(0,10000) for _ in range(x)]
    
#生成含20个数的列表
nums(20)
# print(nums_lst)
#对列表进行排序
nums_lst.sort()

#依次弹出末尾的数(排序后末尾的数最大)
max1 = nums_lst.pop()
max2 = nums_lst.pop()
max3 = nums_lst.pop()

print('第一大: {}\n第二大: {}\n第三大: {}'.format(max1,max2,max3))
