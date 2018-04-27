#/usr/bin/env python
# -*- coding: utf-8 -*-
# 输入一个英文句子，翻转句子中单词顺序

def revers_sentence():
    '''
    反转输入的句子中单词，不反转单词内的字符
    
    反转前：abc 123
    反转后：123 abc
    '''
    
    sentence = input('请输入一段句子: ')
    print('\n反转前的句子是：{}'.format(sentence))
    
    lst1 = sentence.split(' ') # 保留空格
    lst2 = lst1[::-1]
    print('\n反转后的句子是：',end='')
   
    count = 0
    for i in lst2:
        count += 1
        if count == len(lst2): # 当打印到最后一个单词时换行
            print(i)
        else:
            print(i,end=' ')
             
   
revers_sentence()
