# -*- coding: UTF-8 -*-
# list search
list=[]
print("请输入你的列表，输入'quit'退出")
while True:
    tmpinput=input()
    if tmpinput=="quit":
        print(list)
        break
    list.append(tmpinput)

print('输入你想查的元素 x')
x=input()
i=list.count(x)
if i==0:
    print("0")
else:
    print("1")

