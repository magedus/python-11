f1=1
f2=1
print(f1)
print(f2)
for i in range(98):
    f1,f2=f2,f1+f2
    print(f2)
