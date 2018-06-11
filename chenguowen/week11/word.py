#! /usr/bin/env python
# -*- coding: utf-8 -*-

def joinWord(word:str,dict:list,res=[]):
    """
    
    根据字典，从一个抹去空格的字符串里面提取出全部单词组合，并且拼接成正常的句子:
    例如: 输入一个字符串："thisisanexample", 程序输出: "this is an example" 
    word：字符串
    dict：字典
    res：结果输出

    """
    
    res = res[:]
    start = 0
  
    for end in range(start,len(word)):
        if word[start:end + 1] in dict:
            res.append(word[start:end + 1])
            start = end + 1

    print(res)

wordDict = ['this','is','an','example']
wordStr = 'thisisanexample'

joinWord(wordStr,wordDict)
