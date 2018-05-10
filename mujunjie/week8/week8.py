#1、实现一个函数用于判断字符串str2是否是str1的子串。如果是，则该函数返回str2在str1中首次出 现的地址；否则，返回None。
def subset(sub, str1):
    index = 0
    index2 = 0
    while True:
        if index2 >= len(str1)  or index == len(sub)  :
            break
        if sub[index] != str1[index2]:
            if index == 0:
                index2 += 1
            index = 0
            #       print(str2[index2])
            continue
        else:
            index += 1
            index2 += 1
    print(index,index2)
    if index == len(sub) :
        return index2 - index
    else:
        return -1
a = "*19632587411"
b = "741"
c = subset(b,a)
print(subset(b,a))




#2、给定一个整型列表，请实现从其中找出2个数的和为某一个指定的值？
#如：lst =[1,5,2,7,4,9]，指定的目标值为11，可以从中找出 2和9之和为11 
#温馨提示：请于5月13日晚之前提交

lst = [1,5,2,7,4,9,3,8,6]
const = 11

def sumlst(lst,counst):
    x = []
    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            if lst[i] + lst[j] == const:
                x.append([lst[i],lst[j]])
    return x


print(sumlst(lst,a))








