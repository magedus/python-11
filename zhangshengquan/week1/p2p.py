#!/usr/bin/env python
# -*- coding: utf-8 -*-

# print(2,end=" ")
# for j in range(3,100000,2):
#     for i in range(3,j,2):
#         if  j%i == 0:
# #            print(j,"这不是质数")
#             break
#     else:
#         print(j,end=" ")


# import math
# n = 100
# primenumber = []
# for x in range(2,100):
#     for i in primenumber:
#         if x % i == 0:
#          break
#     else:
#        print(x)
#        primenumber.append(x)
#



# triangle=[[1],[1,1]]
# n=6
# for i in range(2,6):
#     pre = triangle[i-1]
#     cur= [1]
#     for j in range(0,i-1):
#         cur.append(pre[j]+pre[j+1])
#     cur.append(1)
#     triangle.append(cur)
# print(triangle)

#求出100以内的素数：这个代码比下面的代码效率要高很多倍。

import datetime
import math
n=10000
primenumber = []
flag = False
count=0
start=datetime.datetime.now()
for x in range(2,n):
    for i in primenumber:
        count += 1
        if x % i == 0 :
            flag = True
            break
        if i >= math.ceil(math.sqrt(x)):
            flag = False
            break
    if not flag:
        primenumber.append(x)

delta=(datetime.datetime.now() - start).total_seconds()
print(len(primenumber))
print(count)
print(delta)


#求出100以内的素数：

# import datetime
# import math
# n=10000
# primenumber = []
# count=0
# start=datetime.datetime.now()
# for x in range(2,n):
#     for i in primenumber:
#         count +=1
#         if x % i == 0:
#          break
#     else:
#  #      print(x)
#        primenumber.append(x)
#
# delta=(datetime.datetime.now() - start).total_seconds()
# print(len(primenumber))
# print(count)
# print(delta)










































