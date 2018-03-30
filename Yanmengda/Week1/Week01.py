#Week01作业

"""
1、搭建好pyenv环境，理解local、global、shell 3种方式区别，安装部署完成jupyter并运行
2、打印出100以内的斐波那契数列，使用2种方法实现
3、使用 Python 实现随机生成 200 无重复激活码（或者优惠券），字符串长度大于5以上
"""

#No.2
#(1)
i = 1
j = 1
print(i)
print(j)
for _ in range(50):
    i,j = j,i+j
    if i+j < 100:
        print(i+j)

#(2)
fb = [1,1]
while True:
    fb.append(fb[-2] + fb[-1])
    if fb[len(fb)-1] < 100:
        continue
    else:
        fb.pop()
        break
print(fb)


#No.3

import random  
import string  

result = []
source = list(string.ascii_letters+string.digits)

num = 10
length = 15

for i in range(10):
    result.append(str(i))
    while  len(result) < num:
        tmp = ''
        for j in range(length):
            tmp += random.choice(source)
        if tmp in result:
            pass
        else:
            result[i]=tmp
            print(result[i])
            break
