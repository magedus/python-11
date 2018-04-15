print(0)
print(1)
a = 0
b = 1
while True:
    c =a + b
    a = b
    b =c
    if c > 100:
        break
    print(c)
