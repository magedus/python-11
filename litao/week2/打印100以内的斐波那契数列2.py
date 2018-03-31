a = 1
b = 1

print(a)
print(b)

while True:
    a += b
    if a > 99:
        break
    print(a)
    b += a
    if b > 99:
        break
    print(b)