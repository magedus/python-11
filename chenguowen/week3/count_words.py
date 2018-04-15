#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Description: count words in a file

#import modules
import collections

#define variables
file_name = 'words.txt'
open_file = open(file_name,'r',encoding='utf-8')
#split words into a list
word_orig_lst = open_file.read().split()

#convert list into set  to remove duplicate word
word_set = set(word_orig_lst)

#convert set into list because set has no index
word_uniq_lst = list(word_set)

#dict can count the number of word
word_dict = {}

for i in range(len(word_uniq_lst)):
    word_dict[word_uniq_lst[i]] = 0

    for j in range(len(word_orig_lst)):
        if word_uniq_lst[i] == word_orig_lst[j]:
            word_dict[word_uniq_lst[i]] += 1

print('The number of word in the words.txt is: \n',word_dict)
close_file = open_file.close()
