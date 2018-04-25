# 统计当前目录下text文本中单词出现个数
import re


with open("./text") as f:
    a = f.read().rstrip().split()
    b = {} 
    for i in a:
        i = re.search("\w+",i).group()
        if i in b:
            b[i] += 1
        else:
            b[i] = 1
print(a)
print()
print()
print()
print()





print(b)




