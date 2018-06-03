# 输入一个英文句子,翻转句子中的单词顺序,但单词内字符的顺序不变
def inversion(input_str):
    a = input_str.split(" ")
    a.reverse()
    return a


base_str = "long long ago , there is a montain ."
result = inversion(base_str)
print(result)
