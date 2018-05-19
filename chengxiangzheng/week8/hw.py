1.实现一个函数用于判断字符串str2是否是str1的子串。如果是，则该函数返回str2在str1中首次出 现的地址；否则，返回None。
def strcxz(_):
    str1=str(input(">>>"))
    str2=str(input(">>>"))
    if str2 in str1:
        print("Yes")
        print(str1.find(str2))
        print(str1.index(str2))
    else:
        print("None")
    
strcxz(_)
2.给定一个整型列表，请实现从其中找出2个数的和为某一个指定的值？
lst=[1,5,2,7,4,9]
n=11
for x in lst:
    y = n - x
    if y in lst:
        print("lst exist {} plus {} equals {}".format(x,y,n))
    else:
        print("None")
3.随机生成
import random
lst=[random.randint(0,10) for _ in range(10)]
print(lst)
n=int(input(">>>"))
for x in lst:
    y = n - x
    if y in lst:
        print("lst exist {} plus {} equals {}".format(x,y,n))
    else:
        print("None")