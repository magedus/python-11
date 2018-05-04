import random
import time

a=[1,2,3,4,5]
b=[]
c=[]
flag=False
i=0
while len(b) < 5:
	i=random.randint(0,4)
	if i not in b:
		b.append(i)
for i in b:
	c.append(a[i])
print(c)


