# 实现一个函数用于判断字符串str2是否是str1的子串。如果是，则该函数返回str2在str1中首次出 现的地址；否则，返回None。


def find_sub(s1: str, s2: str):
    """
    直接使用字符串索引方式
    :param s1:
    :param s2:
    :return:
    """
    if not s1 or not s2:
        raise ValueError('input not allow empty string')
    try:
        i = s1.index(s2)
    except ValueError:
        return None
    return i


def find_sub2(s1: str, s2: str):
    """
    对目标字符串进行循环，然后索引进行比较
    :param s1:
    :param s2:
    :return:
    """
    if not s1 or not s2:
        raise ValueError('input not allow empty string')
    c = s2[0]
    s2_length = len(s2)
    for i, s in enumerate(s1):
        if s == c:
            if s1[i: i+s2_length] == s2:
                return i


print(find_sub('11', '1eee'))
print(find_sub2('weqr', 'e'))

# 给定一个整型列表，请实现从其中找出2个数的和为某一个指定的值
# 如：lst =[1,5,2,7,4,9]，指定的目标值为11，可以从中找出 2和9之和为11
#


def find_dst_value(target: int, targets: list):
    """
    time complexity O(N^2)
    :param target:
    :param targets:
    :return:
    """
    length = len(targets)
    for i in range(length):
        for j in range(i, length):
            if targets[i] + targets[j] == target:
                return targets[i], targets[j]


lst = [1, 5, 2, 7, 4, 9]
t3 = 3
print(find_dst_value(t3, lst))
