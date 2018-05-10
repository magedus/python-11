#-*- coding: utf-8 -*-
# 随机生成20个数字，并且筛选出其中最大的3个数 


import random


nums = []
for i in range(20):
    nums.append(random.choice(range(100)))
print(nums)

for m in range(len(nums)):
    for n in range(m+1, len(nums)):
        if nums[m] < nums[n]:
            nums[m], nums[n] = nums[n], nums[m]


print(nums)  
print(nums[0], nums[1], nums[2])