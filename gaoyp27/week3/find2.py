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
if x in list:
    print("1")
else:
    print("0")

