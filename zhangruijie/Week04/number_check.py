import random

for _ in range(200):
    n= random.randint(10000,99999)
    #print(n)
    nlist= list(str(n))
    if nlist[0] == nlist[-1] and nlist[1] == nlist[-2]:
        print("{} is palindrome number".format(n))
    
