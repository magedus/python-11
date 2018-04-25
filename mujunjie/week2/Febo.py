a = 1
b = 1
while True:
    c = a+b
    a = b
    b = c
    if c >100 :
        break
    print(c,end= " ")
print()




B = []
for i in range(100):
    if i == 0:
        B.append(i)
        continue
    if i == 1:
        B.append(i)
        continue
    if B[i-2] + B[i-1] < 100:
         B.append(B[i-2] + B[i-1])
    else:
         break
print(B)
