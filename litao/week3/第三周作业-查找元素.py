#1.给出任意一个列表，请查找出X元素是否在列表里，如果在返回1，不存在返回0
import random


args = ("please Enter Your argments: ") #用户输入的元素
randlist = []

#生成随机数据

for _ in range(100):
    randlist.append(random.randint(0,100))

#判断用户输入的是否在列表里，为了提高查找效率故用了集合

randset = set(randlist)
if args in randset:
    print(1)
else:
    print(0)