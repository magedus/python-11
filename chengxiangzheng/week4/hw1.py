n=input(">>>")                  #回文数判断
flag=True
n_new=n[::-1]
print(n_new)
for i in range(len(n)):
    if n[i]==n_new[i]:
        flag=True
    else:
        flag=False
if flag==True:
    print(n+"是回文数")
else:
    print(n+"不是回文数")