# 1、python 中如何实现单例模式，尽可能多的写出实现方式
# 2、两个有序数组，分别拥有m和n的长度，求其合并后的第k个值
# 3、 将逆转波兰式转化为中序表达式（自行查询逆波兰式、中序表达式相关资料）
# 举例: 输入 {"5", "8", "4", "/", "+"}，输出 "(5+(8/4))"
# 孩子们，请大家尽可能的在达到相关进度的情况下完成作业

# class SingleInstance:
#     def __init__(self):
#         print('hello world')
#
#
# s = SingleInstance()
# print(s)

# a = [10,20,30,40,50]
# b = [1,2,3,4,5,6,7,99,100]
# def searchk(m,n,array1,array2,k,lst=[]):
#     if n>m:
#         while m>0 and n>0:
#             if array1[m-1]>array2[n-1]:
#                 lst.append(array1[m-1])
#                 m -=1
#             else:
#                 lst.append(array2[n-1])
#                 n-=1
#         if n>0:
#             lst.extend(b[:n][::-1])
#     return lst[len(lst)-k]
#
#
# print(searchk(len(a),len(b),a,b,7))
