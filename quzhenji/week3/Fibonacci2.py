def fun(n):
    if n<=1:
        return n
    else:
        return fun(n-2)+fun(n-1)

num = int(input('>>>'))
for i in range(num+1):
    print(fun(i))