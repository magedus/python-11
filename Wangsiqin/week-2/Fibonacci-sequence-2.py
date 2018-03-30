a = 0
b = 1
print(a,b,end=' ')
while True:
    a += b
    b += a
    if a >= 100:
        break
    print(a,b,end=' ')
