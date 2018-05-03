import math


s1 = input('please input a sentence>>>')
lst = list(s1.split(' '))
print(lst)
length = len(lst)
for i in range(length-1,math.ceil(length/2)-1,-1):
    lst[i],lst[length-1-i] = lst[length-1-i],lst[i]

print(' '.join(lst))