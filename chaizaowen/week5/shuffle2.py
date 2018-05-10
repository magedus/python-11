import random

alist = [1,2,3,4,5]

def shuf(nums):
    alist_shuffle = []
    while alist:
        i = random.choice(alist)
        alist.remove(i)
        alist_shuffle.append(i)
    return alist_shuffle

print(shuf(alist))