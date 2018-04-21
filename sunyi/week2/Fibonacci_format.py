a = 1
b = 1
index = 2
print('{0},{1}'.format(0, 0))
print('{0},{1}'.format(1, 1))
print('{0},{1}'.format(2, 1))
while True:
    c = a + b
    a = b
    b = c
    index += 1
    if c < 100:
        print('{0},{1}'.format(index, c))
    else:
        break

