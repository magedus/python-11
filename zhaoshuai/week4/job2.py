import random
lit=[]
for i in range(20):
      lit.append(random.randint(0, 200))
print(lit)
tempList=list(sorted(lit,reverse=True))
for i in range(3):
      print(tempList[i])