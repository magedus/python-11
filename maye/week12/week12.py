# 1、实现一个可迭代的类
# # 2、给出一个无序的整型列表，找出最长连续元素序列的长度，时间复杂度要求在线性时间内。
# # 例如：
# #     输入：[8,1,9,3,2,4]，那么其最长连续序列是[1,2,3,4]，即输出长度为4
# # 3、输入一个字符串，求不含有重复字母的最长子串的长度
# # 例如：
# #    输入字符串'aaa'，其不含有重复字母的最长子串为‘a’，输出长度为1
#第一题
# class Iter:
#
#     def __init__(self,num):
#         self.num = num
#
#     def _sum(self):
#         sum = 0
#         for x in range(self.num):
#             yield sum + x
#
#     def __del__(self):
#         print('leaving')
#
# for x in Iter(5)._sum():
#     print(x)


# lst1 = [8,1,9,18,10,11,12,15,16,3,2,4]
# def long_len(lst:list):
#     array = sorted(lst)
#     count = 1
#     long = 0
#
#     for i,x in enumerate(array):
#         if i==0:
#             continue
#         if array[i] == array[i-1]+1:
#             count +=1
#             if count > long:
#                 long = count
#         else:
#             count = 1
#     return long
# print(long_len(lst1))


# while True:
#     a = input('>>>')
#     if isinstance(a.strip(),str):
#         break
#
# def long_sub(str:str):
#     return len({x for x in str})
# print(long_sub(a))
