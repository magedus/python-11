import random
lst=[]
s=0
for i in range(20):
    a = random.random()
    n = random.randint(0, 30)
    s=int(a*10**n)
    lst.append(s)
lst.sort()
print(lst[-3:])

print('please type five numebers')
a=input('>>>')
for i in range(5//2+1):
    if a[i]!=a[-i-1]:
        print('no')
        break
else:
    print('yes')

