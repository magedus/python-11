a = 1
b = 0
c = 1

print(a)
while True:
    b = a + c
    if  b >= 100:
        break
    print(b)
    a = b + c
    if a >= 100:
        break
    print(a)
    c = b + a
    if c >= 100:
        break
    print(c)
