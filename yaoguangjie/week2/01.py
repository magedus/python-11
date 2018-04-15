ls = [1]*15
print(ls[0])
print(ls[1])
for i in range(2,15):
     ls[i] = ls[i - 1] + ls[i - 2]
     if ls[i] < 100:
          print(ls[i])
     else :
         break
