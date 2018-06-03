#实现一个函数用于判断字符串str2是否是str1的子串。如果是，则该函数返回str2在str1中首次出 现的地址；否则，返回None。

def child_str(str1,str2):
    if str2 in str1:
        return str1.find(str2)
    else:
        return None

str1 = 'abcdefg'
#str2 = 'ef'
str2 = 'efa'

print(child_str(str1,str2))


