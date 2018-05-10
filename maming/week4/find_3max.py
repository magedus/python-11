# -*- coding:utf-8 -*-
# -*— author: maming -*-

import random

alpha=[  int(random.randrange(10,10000)*random.random()/10) for _ in range(20)]

print("beagin:",alpha)
find_max=[]

for i in range(3):
    find_max.append(max(alpha))
    alpha.pop(alpha.index(max(alpha)))

print("three max number is:",find_max)
print("end:",alpha)
