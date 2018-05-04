#方法1
#定义递归
def recur_fibo (n):
    if n <= 1:
        return n
    else:
        return (recur_fibo(n-1) + recur_fibo(n-2))
n=0
while True:
    if recur_fibo(n) > 100:
        break
    else:
        print(recur_fibo(n),end = '   ')
    n +=1