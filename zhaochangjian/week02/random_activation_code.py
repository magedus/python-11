# -*- coding: utf-8 -*-sss
#使用 Python 实现随机生成 200 无重复激活码（或者优惠券），字符串长度大于5以上
import random


activation = set()
while True:
    if len(activation) == 200:
        break
    else:
        activation.add(random.choice(range(10000, 99999)))


for i in activation:
    print(i)
