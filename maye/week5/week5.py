import random

d1={'socks':10,'shoes':20,'fflop':30,'necklace':40}
def prod(depot):
    lst=[[k]*v for k,v in depot.items()]
    lst1=[lst[i][j] for i in range(len(lst)) for j in range(len(lst[i]))]
    return random.choice(lst1)
print(prod(d1))

#打乱随机
alist=[1,2,3,4,5]
random.shuffle(alist)
print(alist)
