#打印出小于n的所有素数（继续优化，提高效率！）
n=int(input())
count=0
for i in range(2,n):
    for j in range(2,i):
        if i%j==0:
            #print("not prime number")
            break
    else:
        count+=1
        print("第"+str(count)+"个prime number为"+str(i))
print("小于"+str(n)+"的素数一共为:"+str(count)+"个")