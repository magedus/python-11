#! /usr/bin/env python
# -*- coding: utf-8 -*-

def check_dup_character(args:str):
    """
    
    实现一个函数，输入字符串，判断该字符串是否不含有重复字符
    Exsample: check_dup_character('abcdef')
    """   

    no_dup_character = []
    dup_character = []
    
    for i in range(len(args)):
        if args.count(args[i]) >= 2:
            
            if args[i] in dup_character:
                continue
            else:
                dup_character.append(args[i])
                         
        else:
              no_dup_character.append(args[i])
        
        
    if len(dup_character) >= 1:
        print('字符串{}中有重复字符：{}'.format(args,dup_character))
    else:
        print('字符串{}中没有重复字符.'.format(args))
            
check_dup_character('Hello Python')
