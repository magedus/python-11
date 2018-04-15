#随机生成20个数字，筛选出其中最大的3个数。
import random
random_list = []
for i in range(1,21):
    random_list.append(random.randint(-100,100))
random_list.sort(reverse=True)
print(random_list[0],random_list[1],random_list[2])

