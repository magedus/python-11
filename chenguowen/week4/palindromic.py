#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 判断是否是回文数

def palindromic():
    while True:
        num = input('请输入一个5位正整数: ')
    
        #判断输入的是否是5位正整数
        if num.isdigit() and len(num) == 5:
            
            #判断是否是回文数
            if num == num[::-1]:
                print('你输入的{}是回文数.'.format(num))
                break
            else:
                print('你输入的{}不是回文数.'.format(num))
                break
        else:
            print('你输入的{}不是一个5位正整数，请重新输入: '.format(num))

        
palindromic()
