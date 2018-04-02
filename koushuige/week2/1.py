# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89
# 方法一
# a =1
# b =0
# while True:
#     c = a + b
#     a = b
#     b = c
#     if  c>=100:
#         break
#     print(c)

def Fib(a,b):
    c =a + b
    a = b
    b = c
    Fib(a,b)
    if c >= 100:
        return c
ret=Fib(1,1)
print(ret)






