#-*- coding: utf-8 -*-
#任一个英文的纯文本文件，统计其中的单词出现的个数

import os

word_count = {}
with open('english_articles') as f:
    words = f.readline().split()
    #print(words)
    for w in words:
        word_end_with = [',', '.', '!', ':', ';']
        for s in word_end_with:
            if w.endswith(s):
                w = w.split(s)[0]
        if not w in word_count:
            word_count[w] = 1
        else:
            word_count[w] +=1
            
for k, v in word_count.items():
    print('{0} count: {1}'.format(k, v))
    