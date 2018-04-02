print(1)
a = 0
b = 1
while True:
    c = a+b
    if c>100:
        break
    a = b
    b = c
    print(c)