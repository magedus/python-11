# 打乱一个排好序的list对象alist，alist=[1,2,3,4,5]
import random


def shuffle_list(x):
    backup = x[:]
    while True :
        if backup == x:
            random.shuffle(x)
        else:
            break
    return x


alist = [1, 2, 3, 4, 5]
alist_shuffle = shuffle_list(alist)
print(alist_shuffle)
