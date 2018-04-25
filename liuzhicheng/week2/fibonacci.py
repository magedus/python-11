# Solution 1
n = 100
a = 0
b = 1
while a < n:
    print(a, end=' ')
    c = a+b
    a = b
    b = c
print()

# Solution 2
n = 100
fib = [0, 1]
print(fib[0], end=' ')
while fib[-1] < n:
    print(fib[-1], end=' ')
    fib.append(fib[-1]+fib[-2])
print()