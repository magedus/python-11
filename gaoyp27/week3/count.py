# -*- coding: UTF-8 -*-
# count word
file_name = "test"

line_counts = 0
word_counts = 0
character_counts = 0

with open(file_name, 'r') as f:
    for line in f:
        words = line.split()
        word_counts += len(words)


print ("word_counts ", word_counts)
