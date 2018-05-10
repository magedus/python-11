# -*- coding: UTF-8 -*-
# reverse  setence

s1=input('please input a sentence>>>')


def setence_reverse(w):
    print(w)
    w=w.split()
    w.reverse()
    print(" ".join(w))

setence_reverse(s1)