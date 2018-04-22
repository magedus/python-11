# -*- coding: UTF-8 -*-
# Python 斐波那契数列实现

# 获取用户输入数据
num = int(input("你需要几项？"))

n1=0
n2=1
count=2

if num<=0:
    print("请输入一个正整数! ")
elif num==1:
    print("斐波那契数列：%d"%n1)
else:
    print('斐波那契数列：%d,%d' %(n1,n2),end=",")
    while count<num:
        nth=n1 + n2
        print(nth,end=",")
        n1=n2
        n2=nth
        count+=1


# -*- coding: UTF-8 -*-
# Python 斐波那契数列求值
# 获取用户输入数据
num = int(input("多少以内的斐波那契数列？"))

n1=0
n2=1
nth=0

if num<=0:
    print("请输入一个正整数! ")
elif num==1:
    print("斐波那契数列：%d"%n1)
else:
    print('斐波那契数列：%d,%d' %(n1,n2),end=",")
    while n1+n2<num:
        nth=n1 + n2
        print(nth,end=",")
        n1=n2
        n2=nth


# -*- coding: UTF-8 -*-
# Python 斐波那契数列求值
# 获取用户输入数据
num = int(input("多少以内的斐波那契数列？"))

n1=0
n2=1
nth=0

if num<=0:
    print("请输入一个正整数! ")
elif num==1:
    print("斐波那契数列：%d"%n1)
else:
    print('斐波那契数列：%d,%d' %(n1,n2),end=",")
    while nth<num:
        nth=n1 + n2
        if nth<=100:
            print(nth,end=",")
        n1=n2
        n2=nth

#求斐波那契数列的第n项的
# 获取用户输入数据
num = int(input("你需要第几项？"))

n1=0
n2=1
count=2

if num<=0:
    print("请输入一个正整数! ")
elif num==1:
    print("斐波那契数列：%d"%n1)
else:
    print('斐波那契数列：%d,%d' %(n1,n2),end=",")
    while count<=num:
        nth=n1 + n2
        n1=n2
        n2=nth
        count+=1
    if count==num:
        print(nth,end=",")


