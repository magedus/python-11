#lst = [1,1]
#for i in range(2,20):
#    if lst[i-1] + lst[i-2]>100:
#        break
#    lst.append(lst[i-1] + lst[i-2])
#print(lst)


lst = [1,1]
i = 1
while True:
    i +=1
    if lst[i-2] + lst[i-1] > 100:
        break
    lst.append(lst[i-2] + lst[i-1])
    print(lst)

lst = [1,1]
a=0
for i in range(2,102):
    lst.append(lst[i-1]+lst[i-2])
    if i == 101:
        a=lst[i-1] + lst[i-2]
print(a)


import random
lst=[]
#生成26个大写的字母
for x in range(65,91):
    a=str(chr(x))  #生成对应的ASCII码对应的字符串
    lst.append(a)
#生成26个小写字母
for x in range(97,123):
    a=str(chr(x))  #生成对应的ASCII码
    lst.append(a)
#生成10个数字
for x in range(10):
    lst.append(str(x))
i=0
def gen_code():
    s=''
    for _ in range(16):
        a=random.choice(lst)
        s+=a
    print(s)
for _ in range(200):
    gen_code()
'''
global是全局环境
shell是绘画级别
local当前环境
'''
