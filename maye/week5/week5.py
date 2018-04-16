import random

lst=[]
lst1=[]

d={'socks':10,'shoes':20,'fflop':30,'necklace':40}
for k,v in d.items():
    lst.append(k)
    lst1.append(v)
#print(lst)

for i in range(len(lst1)):
    m=int(lst1[i])
    for j in range(m-1):
        lst.append(lst[i])
a=random.choice(lst)
#print(lst,lst.count('necklace'))
print(a)

#打乱随机
alist=[1,2,3,4,5]
random.shuffle(alist)
print(alist)
