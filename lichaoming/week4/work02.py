#随机生成20个数字
import random
nums = []
while len(nums)<=20:
    num = random.randint(0,100)
    nums.append(num)
print(nums)

#筛选出其中最大的3个数
count = 0
while count < 3:
    biggest_num = max(nums)
    print(biggest_num)
    nums.remove(biggest_num)
    count +=1