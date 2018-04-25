import random
lst = []
count = 0
l1 = 'abcdefghigklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
while True:
    count += 1
    a = ''
    for j in range(1,11):
        i = random.choice(l1)
        a += i
    lst.append(a)
    if count ==20:
        break
print(lst)