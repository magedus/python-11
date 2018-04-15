lst=[]
for i in range(13):
    if i<=1:
        lst.append(i)
    else:
        lst.append(lst[i-2]+lst[i-1])
print(lst)


lst2=[]
n=0
sum=0
while sum<100:
    if n<=1:
        lst2.append(n)
    else:
        lst2.append(lst2[n-1]+lst[n-2])
        sum=lst2[-1]+lst2[-2]
    n=n+1
print(lst2)