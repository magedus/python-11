#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/3/31 上午10:33
__author__ = 'ZhanWei'
iterations = int(input("Number of iterations: "))  
cont = 1  
result = ""  
  
if iterations > 0:  
    fibonacci1 = 0  
    fibonacci2 = 1  
  
    result = result + "" + format(fibonacci1)  
    result = result + ", " + format(fibonacci2)  
  
    while cont < iterations:  
        temp = fibonacci2  
        fibonacci2 = fibonacci1 + fibonacci2  
        fibonacci1 = temp  
        result = result + ", " + format(fibonacci2)  
        cont = cont + 1  
  
print("Fibonacci: " + result) 