# 现有两元祖   (('a'),('b'),('c'),('d')) ,请使用Python中的匿名函数生成列表 [ {'a':'c'｝,{'c':'d'}]
a =  (('a'),('b')),(('c'),('d'))
b = [{x[0], x[0]} for x in a]
print(b)



# 输入一个英文句子,翻转句子中的单词顺序,但单词内字符的顺序不变


def rev_sentence(s: str):
    s_list = s.split()
    s_list.reverse()
    rev_s = ' '.join(s_list)
    return print(rev_s)


s1 = "I love everyone in magedu , especially the '不动教练' and MissLi"
rev_sentence(s1)


def rev_sentence2(s:str):
    s = ' '.join(reversed(s.split()))
    return s


s = 'magedu is a great group for thoes who want to learn'
print(rev_sentence2(s))