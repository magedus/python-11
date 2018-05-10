#1、实现一个函数用于判断字符串str2是否是str1的子串。如果是，则该函数返回str2在str1中首次出 现的地址；否则，返回None。
def judgeStr(s1,s2):
    return None if s1.find(s2) == -1 else s1.find(s2)

judgeStr('12345','3')

#2、给定一个整型列表，请实现从其中找出2个数的和为某一个指定的值？
#如：lst =[1,5,2,7,4,9]，指定的目标值为11，可以从中找出 2和9之和为11
lst = [1, 5, 2, 7, 4, 9]
def autoSum(n):
    result = []
    for i in range(len(lst) - 1):
        for j in range(i + 1, len(lst)):
            if n == lst[i] + lst[j]:
                result.append(lst[i])
                result.append(lst[j])
    print(result) if result != [] else print('No result')

autoSum(9)