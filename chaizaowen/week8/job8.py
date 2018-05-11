#1.实现一个函数用于判断字符串str2是否是str1的子串。如果是，则该函数返回str2在str1中首次出 现的地址；否则，返回None。

def substr(str1: str,str2: str):
    '''
    require len(str1) > len(str2)
    :param str1: str
    :param str2: str
    :return:
    '''
    if str1.find(str2) == -1:
        return
    return str1.find(str2)

print(substr('test','st'))
print(substr('MissLi&teacherBudong','tangdou'))

#2.给定一个整型列表，请实现从其中找出2个数的和为某一个指定的值？如：lst =[1,5,2,7,4,9]，指定的目标值为11，可以从中找出 2和9之和为11

lst =[1,5,2,7,4,9]
dest = 11

def findit(lst: list,dest: int):
    target = []
    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            if lst[i] + lst[j] == dest:
                target.append((lst[i],lst[j]))
    return target

print(findit(lst,dest))

# for i in range(len(lst)):
#     for j in range(i+1,len(lst)):
#         if lst[i] + lst[j] == 11:
#             print(lst[i],lst[j])