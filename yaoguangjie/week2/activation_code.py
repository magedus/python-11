import string
import random
q=[]
count=0
while True:
 chars= string.ascii_letters + string.digits
 s=random.choices(chars,k=6)
 tem=s[0]+s[1]+s[2]+s[3]+s[4]+s[5]
 if tem in q:
     continue
 q.append(tem)
 count+=1
 if count==200:
     break
 print(q)




