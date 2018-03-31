# -*- coding: UTF-8 -*-
# Python 生成200个无重复激活码/优惠劵


#群内同学老师交流提到的方法使用uuid随机生成32位验证码
import uuid
for i in range(200):
    print (uuid.uuid4())


# 自己尝试使用的方法，有点问题
import random
list='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
#生成26个大写字母
for x in range(4):
    a=random.choices(list, k=16)
    print (a)





