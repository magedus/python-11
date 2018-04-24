#查找元素x是否在列表中
target=[1,4,2,5,7,8,6]
x=int(input("please input a integer number"))
if x in target:
    print(1)
else:
    print(-1)

#统计单词出现的个数
str="I like study study study."
target="study"
nums=str.count(target)
print(nums)


