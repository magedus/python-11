import random
lst=[]
s=0
for i in range(20):
    a = random.random()
    n = random.randint(0, 320)
    s=int(a*10**n)
    lst.append(s)
lst.sort()
print(lst[0:3])

print('please type five numebers')
a=input('>>>')
for i in range(5):
    if a[i]!=a[-i-1]:
        print('no')
        break
else:
    print('yes')
