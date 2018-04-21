# -*- coding: utf-8 -*-
#打印出100以内的斐波那契数列，使用2种方法实现

import  datetime

#递归
def fib1(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib1(n-1) + fib1(n-2)

#递归      
def fib2(n):
    memory = {0:0, 1:1}
    if not n in memory:
        memory[n] = fib2(n-1) + fib2(n-2)
    return memory[n]
    
#交换  
def fib3(n):
    a, b = 0, 1
    for n in range(n):
        a, b = b, a + b
    return a

t = datetime.datetime.now()
print(fib3(100))
delta = (datetime.datetime.now() - t).total_seconds()
print(delta)