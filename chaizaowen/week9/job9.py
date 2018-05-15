
# 1、请实现函数 new_counter ，使得调用结果如下：
# c1 = new_counter(10)
# c2 = new_counter(20)
# print（c1(), c2(), c1(), c2()）
# outputs ：
# 11 21 12 22

def new_counter(num: int):
    def inc(step=1):
        nonlocal num
        num += step
        return num
    return inc

c1 = new_counter(10)
c2 = new_counter(20)
print(c1(), c2(), c1(), c2())



# 2、实现一个函数，输入字符串，判断该字符串是否不含有重复字符

def norepeat():
    while True:
        str1 = input('>> ').strip()
        if str1 == 'quit':
            return
        for i in range(len(str1)):
            if str1.count(str1[i]) > 1:
                return 'the string has repeat '
        else:
            return 'the string has not repeat'

print(norepeat())