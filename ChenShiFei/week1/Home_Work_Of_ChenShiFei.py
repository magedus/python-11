#method1
n=0
m=1
while m<100:
    print(m,end=' ')
    n,m=m,n+m
print()
print("---------------------")
#method2


import random
lt=list(range(10000,100000))
b=random.sample(lt,200)
print(b)

#method for making 200 random strings
import random
import string
lst=[]
for i in range(200):
    a = ("".join(random.choices(string.ascii_letters + string.digits, k=6)))
    lst.append(a)
#print(set(lst))
#print(len(set(lst)))
#for j in range(1,201):
    print("第{:>3}个优惠是:{}".format(i+1,lst[i]))


