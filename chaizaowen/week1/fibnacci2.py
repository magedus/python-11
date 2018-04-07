first = 0
second = 1
cur = 0
print(first,second,end = ' ')

while cur < 100:
    cur = first + second
    print(cur,end = ' ')
    first = second
    second = cur
