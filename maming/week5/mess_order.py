import random 

def mess(alist=[]):
    blist=alist[:]
    print("Before disrupting:{}".format(blist))
    random.shuffle(blist)  
    return blist

alist=[1,2,3,4,5]
print("After disrupting:{}".format(mess(alist))) 

