'''随机生成20个数字，并且筛选出其中最大的3个数'''

import random
l1 = []
for i in range(20):
    l1.append(random.randint(1,100))
    l1.sort()
print(l1[-4:-1])
