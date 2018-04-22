n=int(input(">>>"))         #平方回文数判断
a=int((n**0.5))
print(a)
if a**2==n:
    print(str(n)+"平方回文数")
else:
    print(str(n)+"非平方回文数")