#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# check a element is in a list

# import module
import random,string


#define list
str1 = ' '.join(random.choices(string.ascii_letters + string.digits,k=10))

#judge element
if 'x' in str1:
    print(1)
else:
    print(0)


