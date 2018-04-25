a='When your friend speaks his mind you fear not the "nay" in your own mind, nor do you withhold the "ay." '
lst=a.split()
def reouter(lst1=None):
    if lst1 is None:
        lst1=[]
    for i in range(len(lst1)//2+1):
        lst1[i],lst[-i-1]=lst[-i-1],lst[i]
    return ' '.join(lst1)

print(reouter(lst))



m=(('a'),('b'))
n=(('c'),('d'))
lst=list(m)
lst[1]=list(n)[0]
#print(dict(zip(lst,lst1)))
print([dict((i,)) for i in (lambda x,y:zip(x,y))(lst,list(n))])
