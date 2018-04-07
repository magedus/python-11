#local、global、shell种方式区别
#pyenv global 修改系统全局的Python环境
#pyenv local  修改当前目录的Python环境
#pyenv shell  修改当前shell的Python环境。此时，当前系统和当前目录中设定的Python版本均会被忽略。
#             且重新打开一个新的shell后，该环境也就失效了

#打印出100以内的斐波那契数列
a = 0
b = 1
while b < 100:
    print(b)
    a, b = b, a+b

#打印出100以内的斐波那契数列
fibs = [0,1]
for i in range(10):
    fibs.append(fibs[-2] + fibs[-1])
fibs

#使用 Python 实现随机生成 200 无重复激活码（或者优惠券），字符串长度大于5以上
import random  
str = ''  
randomdict = {}  
char = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'  
length = len(char)  
for keys in range(200):  
    for v in range(5):  
         str += random.choice(char) 
    randomdict[keys] = str  
    str = ''  
print(randomdict)  