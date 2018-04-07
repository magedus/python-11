# 非递归
def Fib3(max):
    a ,b = 0, 1
    n = b
    L=[]
    while(n < max):
        L.append(b)
        a, b = b, a + b
        n = b
    print(L)
	
def Fib2(max):
    a, b = 0, 1
    n = b
    while(n < max):
        yield b
        a, b = b, a + b
        n = b

# 递归
def Fib1(max):
    L = [1, 1]
    while(L[-1] + L[-2] < max):
        L.append(L[-1] + L[-2])
    print(L)
Fib1(10)






def triangles(n):
    L = [1]
    num =0
    while(num < n):
        yield L
        a = L + [0]
        b = [0] +L
        L = L +[0]
        for i in range(len(a)):
            L[i] = a[i] + b[i]
        num = num + 1

