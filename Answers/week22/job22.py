# 1、给出一个无序的整型列表，找出其最长连续元素序列的长度，时间复杂度要求在线性时间内。
#   举例： 输入[8,1,9,3,2,4]，那么其最长的连续序列是[1,2,3,4]，即输出长度为4


def find_longest_consequence(num):
    d = {}

    for x in num:
        d[x] = 1

    ans = 0

    for x in num:
        if x in d:
            length = 1
            del d[x]
            l = x - 1
            r = x + 1
            while l in d:
                del d[l]
                l -= 1
                length += 1
            while r in d:
                del d[r]
                r += 1
                length += 1
            if ans < length:
                ans = length

    return ans


print(find_longest_consequence([8, 5, 1, 9, 3, 2, 4]))


# 2、给出一个无序的列表（至少包含一个元素），求出其最大连续子列表的和？
#   举例：输入[−2,1,−3,4,−1,2,1,−5,4]，那么连续子列表[4,−1,2,1]有最大值，相加是 6

def max_sub_array_sum(array):
    length = len(array)
    max_so_far = array[0]
    current_max = array[0]
    for i in range(1, length):
        current_max = max(array[i], current_max + array[i])
        max_so_far = max(max_so_far, current_max)
    return max_so_far