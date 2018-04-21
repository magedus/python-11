#solve fibonacci recursively
index = 2
Fibonacci = [0, 1]
while 1:
    Fibonacci.append(Fibonacci[index-1]+Fibonacci[index-2])
    if Fibonacci[index] > 100:
        break
    index = index + 1
del Fibonacci[index]
print(Fibonacci)
