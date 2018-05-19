#输入一个英文句子,翻转句子中的单词顺序,但单词内字符的顺序不变
words = "you are a super student"
words_list = words.split() 
words_list.reverse()
words_reversed = ' '.join(words_list)
print(words_reversed)