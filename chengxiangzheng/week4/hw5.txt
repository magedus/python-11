import random
n=int(input())
list1=[]
for i in range(n):
    a = random.randint(0,1000)
    list1.append(a)
print(list1)
print()
list1.sort()                      #sort排序
print(list1)
print()
for i in range(len(list1)):             #冒泡排序
    for j in range(len(list1)-1-i):
        if list1[j]>list1[j+1]:
            list1[j],list1[j+1]=list1[j+1],list1[j]
print(list1)
print()
print(list1[-3:])