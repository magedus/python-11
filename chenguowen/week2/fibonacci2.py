#!/bin/env python
# -*- coding:utf-8 -*-
#斐波拉契数列

first_number = 0
second_number = 1
sum_number = 0

print(first_number,second_number,end=' ')

while sum_number <= 100:
    #从第3个数开始等于前两值的和    
    sum_number = first_number + second_number
    
    if sum_number <= 100:
        print(sum_number,end=' ')
    
    #更新值
    first_number = second_number
    second_number = sum_number
