#1、请大家将自己本月个人学习进度与课程学习总结上报一份
#2、现有两元祖 (('a'),('b')),(('c'),('d')) ,请使用Python中的匿名函数生成列表 [ {'a':'c'｝,{'c':'d'}]
#3、输入一个英文句子,翻转句子中的单词顺序,但单词内字符的顺序不变

#第二题：
t = (('a'),('b')),(('c'),('d'))
foo = lambda x,y:[{x[0]:y[0]},{y[0]:y[1]}]
print(foo(*t))

#第三题：
def reverse(sentence:str):
    lst = sentence.split(' ')[::-1]
    for i in lst:
        print(i, end=' ')
    print()
