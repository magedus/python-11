#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 随机打乱一个列表
import random

def shuffle_lst(list_name):
        random.shuffle(list_name)
        print('乱序后的列表: {}'.format(list_name))

alist = [1,2,3,4,5]
shuffle_lst(alist)
