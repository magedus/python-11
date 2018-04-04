# 统计当前目录下text文本中单词出现个数
with open("./text") as f:
    a = f.read().rstrip()
    b = {} 
    for i in a:
        if i in b:
            b[i] += 1
        else:
            b[i] = 1
print(a)

print(b)




