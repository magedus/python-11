#判断素数（质数：一个大于1的自然数只能被1和它自身整除）
n=int(input())
for i in range(2,n):
    if n%i==0:
        print("not prime number")
        break
else:
    print("prime number")