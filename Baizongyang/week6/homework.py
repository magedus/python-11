#输入一个英文句子,翻转句子中的单词顺序,但单词内字符的顺序不变
def flipping(sentence=None):
    if sentence == None:
        sentence = input(">>>")
        print('{}:{}'.format('翻转前',sentence))
        lst = sentence.split()
        newList = []
        for i in range(-1,-(len(lst))-1,-1):
            newList.append(lst[i])
        x = ' '.join(newList)
        print('{}:{}'.format('翻转后',x))