def fab(n):
    fib=[1,1]
    for i in range(n-2):
        fib.append(fib[-2]+fib[-1])
    return fib

print(fab(100))
