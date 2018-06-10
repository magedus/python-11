# 1、实现一个可迭代的类

class IterC:
    def __init__(self):
        self.lst = []

    def __iter__(self):
        yield from self.lst

# test
iter_c = IterC()
iter_c.lst.extend([2,3,4,5])
for c in iter_c:
    print(c)

# 2、给出一个无序的整型列表，找出最长连续元素序列的长度，时间复杂度要求在线性时间内。
# 例如：
#     输入：[8,1,9,3,2,4]，那么其最长连续序列是[1,2,3,4]，即输出长度为4

def find_longest_consequence(array:list):
    if not array:
        return 0
    hashset = set(array)
    max_num = 0

    for i in array:
        if i-1 not in hashset:
            j = i
            while i in hashset:
                i+=1
            max_num = max(max_num, i-j)

    return max_num


# test
print('Q2:', 80*'-')
print(find_longest_consequence([8,1,9,3,2,4,5]))

# 3、输入一个字符串，求不含有重复字母的最长子串的长度
# 例如：
#    输入字符串'aaa'，其不含有重复字母的最长子串为‘a’，输出长度为1

def longest_substring_length(s: str):
    length = len(s)
    start = 0
    max_len = 0
    d = {}
    for i in range(length):
        k = s[i]
        if k in d and d.get(k) >= start:
            start = d.get(k) +1
        d[k] = i
        max_len = max(max_len, i-start+1)

    return max_len

# test
print('Q3:', 80*'-')
print(longest_substring_length('aaaabbcdefusqq'))
