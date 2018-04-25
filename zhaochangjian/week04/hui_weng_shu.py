#-*- coding: utf-8 -*-
# 问题描述：一个5位数，判断它是不是回文数。---->https://zh.wikipedia.org/zh-hans/%E5%9B%9E%E6%96%87%E6%95%B0



#judge_integer = 12351
judge_integer = 12321

if str(judge_integer)[::-1] == str(judge_integer):
    print('{0}是回文数.'.format(judge_integer))
else:
    print('{0}不是回文数.'.format(judge_integer))