#100以内的斐波那契数列
a=0
b=1
while True:
    c=a+b
    if c>100:
        break
    a=b
    b=c
    print(c)


#生成激活码
import random
target=""
for i in range(200):
    for j in range(5):
        target =target + str(random.randint(1,100))
    print(target)
