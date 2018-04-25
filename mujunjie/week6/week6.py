'''1、目前学到视频中的18节'''
'''2、现有两元祖 (('a'),('b')),(('c'),('d')) ,请使用Python中的匿名函数生成列表 [ {'a':'c'｝,{'c':'d'}]'''
tuple1 = (("a","b"))
tuple2 = (("c","d"))
print((lambda x,y: [{  x[i]:y[i]   for i in range(len(x))}])(tuple1,tuple2))

'''3、输入一个英文句子,翻转句子中的单词顺序,但单词内字符的顺序不变
温馨提示：本周作业，请于4月29日前提交'''

word = "thie is a apple"

def words_reverse(x):
    print(x)
    x = x.split()
    x.reverse()
    print(" ".join(x))

words_reverse(word)


