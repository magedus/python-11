# 1、请实现函数 new_counter ，使得调用结果如下：
# c1 = new_counter(10)
# c2 = new_counter(20)
# print（c1(), c2(), c1(), c2()）
# outputs ：11 21 12 22


# def new_counter(x):
#     cache = {}
#     def nwe_counter():
#         sum = x + 1
#         if x not in cache.keys():
#             cache[x] = sum
#             return sum
#         else:
#             return cache[x] + 1
#     return nwe_counter

def new_counter(num):
    init_nums = {num: num}

    def _new_counter():
        init_nums[num] += 1
        return init_nums[num]
    return _new_counter


c1 = new_counter(10)
c2 = new_counter(20)
print(c1(), c2(), c1(), c2())
print(c1(), c2(), c1(), c2(), c1(), c2(), c1(), c2(), c1(), c2(), c1(), c2(), c1(), c2(), c1(), c2(), c1(), c2())


# 2、实现一个函数，输入字符串，判断该字符串是否不含有重复字符


def chack_str(str):
    a = list(str)  # 转化成列表
    for i in range(len(a)):
        if str.count(a[i]) != 1:  # 判断单个字符串a[i]出现次数
            return False
    return True


def chack_str2(str):
    lst = list(str)
    set1 = set(lst)
    if len(lst) == len(set1):
        return True
    else:
        return False


str = 'abb'
str1 = 'dkghaslghaoueqowet'
str2 = 'qwertyuioplk'
print(chack_str(str))
print(chack_str2(str))
print(chack_str(str1))
print(chack_str2(str1))
print(chack_str(str2))
print(chack_str2(str2))
