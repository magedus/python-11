#python冒泡排序
list=[1,89,37,98,67,82,12,46,328,15,23,124,65,36,76,83]
print(len(list))
for i in range(len(list)):
    for j in range(len(list)-1-i):
        if list[j]>list[j+1]:
            list[j],list[j+1]=list[j+1],list[j]
print(list)