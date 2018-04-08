#随机生成200个优惠券
import random
list=['@','#','$','%','*','1','2','3','4','5','6','7','8','9','0','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
count=0
for x in range(200):
    s=''
    for x in range(10):
        a=random.choice(list)
        s=s+a
    print(s,end="    ")
    count+=1
    if(count%10==0):
        print()
