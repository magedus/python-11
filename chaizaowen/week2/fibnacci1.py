first = 0
second = 1
cur = 0
print(first)
print(second)

while True:
    cur = first + second
    print(cur)
    first = second
    second = cur
    if cur > 100:
        break
