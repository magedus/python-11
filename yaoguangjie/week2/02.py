cur = 1
pre = 0
total = 0
while True:
     total = cur + pre
     if total > 100:
       break
     pre = cur
     cur = total
     print(total)
