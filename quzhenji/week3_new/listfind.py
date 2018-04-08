import random
str1_src = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
lst1 = []
s1 = set()
length = len(str1_src) - 1

while True:
    if len(s1) == 10:
        break      
    s1.add(str1_src[random.randint(0,length)])
      
for x in s1:
    lst1.append(x)

print(lst1)
    
if "x" in lst1:
    print(True)
else:
    print(False)