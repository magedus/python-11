n=input(">>>")       #打印n以内的回文数
a=[]
for k in range(1,int(n)):
    if str(k)==str(k)[::-1]:
        a.append(k)
print(len(a))
print(a)