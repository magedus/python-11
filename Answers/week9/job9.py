# 1、请实现函数 new_counter ，使得调用结果如下：
# c1 = new_counter(10)
# c2 = new_counter(20)
# print（c1(), c2(), c1(), c2()）
# outputs ：
# 11 21 12 22


def new_counter(num: int):
    def _new():
        nonlocal num
        num += 1
        return num
    return _new


c1 = new_counter(10)
c2 = new_counter(20)
print(c1(), c2(), c1(), c2())

# 2、实现一个函数，输入字符串，判断该字符串是否不含有重复字符


def find_repeat(s: str):
    lst = []
    for i in s:
        if i in lst:
            return 'repeat'
        lst.append(i)


print(find_repeat('aew21'))



