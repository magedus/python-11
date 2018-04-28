#输入一个英文句子,翻转句子中的单词顺序,但单词内字符的顺序不变
#实现方法一：列表追加反向取值
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

#实现方法二：切片处理
def flipping(sentence=None):
    if sentence == None:
        sentence = input('Please enter your sentence:')
        lst = sentence.split()
        print(' '.join(lst[::-1]))
    else:
        lst = str(sentence).split()
        print(' '.join(lst[::-1]))
flipping('how can i do for you')


#现有两元祖 (('a'),('b')),(('c'),('d')) ,请使用Python中的匿名函数生成列表 [ {'a':'c'｝,{'b':'d'}]
tup = (('a'),('b')),(('c'),('d'))
print((lambda x:[{v:k} for k,v in zip(x[1:][0],x[:1][0])])(tup))
