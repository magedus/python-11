n=input(">>>")                  #回文数判断
print(n[::-1])
if n==n[::-1]:
    print(n+"是回文数")
else:
    print(n+"不是回文数")