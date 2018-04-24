#问题描述：一个5位数，判断它是不是回文数。
import random
import math

nums_five = list(str(input("Please Enter Five Numbers:")).strip())
lenth = len(nums_five)
count = 0

for i in range(math.floor(lenth//2)):
    if nums_five[i] == nums_five[-i-1]:
        count += 1
    else:
        break

if count == math.floor(lenth//2):
    print('This number is palindromic number.')
else:
    print('This number is not palindromic number')