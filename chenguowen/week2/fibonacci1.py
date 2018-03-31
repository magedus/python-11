#!/bin/env python
# -*- coding:utf-8 -*-

#斐波拉契数列
first_number = 0
second_number = 1

print(first_number,second_number,end=' ')

for i in range(1,11):
    #从第3个数开始等于前两值的和
    sum_number = first_number + second_number
    print(sum_number,end=' ')
    
    #更新值
    first_number,second_number = second_number,sum_number
