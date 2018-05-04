#输入一个英文句子,翻转句子中的单词顺序,但单词内字符的顺序不变
a=str(input(">>"))
print(a)
b=a.split(" ")
for i in range(len(b)):
    print(b[-1-i],end=" ") 