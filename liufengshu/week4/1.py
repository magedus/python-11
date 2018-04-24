def is_palindrome(n):
    n=str(n)
    m=n[::-1]
    return n==m
L = []
for i in range(10000,100000):
    if(is_palindrome(i)):
        L.append(i)

print(L)