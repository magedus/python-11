#s筛选最大的3个数
import random
target=[]
nums=[]
for _ in range(20):#随机生成20个数
    nums.append(random.randint(1,100))
#print(nums)

nums.sort(reverse=True) #降序排列
for i in range(3): #取最前面3个数，即为最大的3个数
    target.append(nums[i])
print(target)

#回文数判断
nums=[input("please input a five-digit number:")]
num=nums.copy()
num.reverse()
if nums==num:
    print("Yes")
else:
    print("No")






