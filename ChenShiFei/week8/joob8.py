#  1、实现一个函数用于判断字符串str2是否是str1的子串。如果是，则该函数返回str2在str1中首次出 现的地址；否则，返回None。
def find_str(str1, str2):
    if len(str1.split(str2)) == 1:
        return None
    else:
        return len(str1.split(str2)[0])+1



str1 = 'dfawoeihgawaasaeqwea'
str2 = 'z'
str3 = 'f'
print(find_str(str1,str2))
print(find_str(str1,str3))


# 2、给定一个整型列表，请实现从其中找出2个数的和为某一个指定的值？
# 如：lst =[1,5,2,7,4,9]，指定的目标值为11，可以从中找出 2和9之和为11

def fin_num(lst, num):
    result = []
    for i, ii in enumerate(lst):
        if i + 1 > len(lst) - 1:
            break
        for j, jj in enumerate(lst[i+1:]):
            if ii + jj == num:
                result.append((ii,jj))
    return result


lst = [1, 5, 2, 7, 4, 9]
print(fin_num(lst,11))

lst = [1, 5, 2, 7, 4, 9, 1, 5, 5, 11, 12, 3, 7, 7, 8, 6]
print(fin_num(lst, 7))


