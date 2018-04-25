import random
a = []
for i in range(20):
    a.append(random.randint(1,2000))
a.sort()
print(a[-3:])
