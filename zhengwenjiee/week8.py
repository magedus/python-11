# coding: utf-8

# 1 实现一个函数用于判断字符串str2 是否是str1但子串。 如果是， 则该函数返回str2在str1中首次出现的地址；否则， 返回None

str1 = "0123abc*&^"

str2 =" #@eKwjr''owj rojg#0123abc*&^HKUoaejo;arji2[\239089@#%#$!ojo;aje'aw jrjwaojaojro;j"


# if st1 in st2 return ture
def is_in_there(st1, st2):
    if st1 in st2:
        return st2.find(st1[0])
    else:
        return None

str2.find('0') == is_in_there(str1, str2)  # True




# 1 给定一个整型列表， 请实现从其中找出2个数的和为某个指定值


li = [1,2,3,4,5,6,7,8,9,0]


def findsum():
    
    pass
    





