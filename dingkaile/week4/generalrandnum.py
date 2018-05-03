import random

numlit=[]
for i in range(0,20):
	numlit.append(random.randint(1,100))
print(numlit)
for i in range(0,3):
	print(max(numlit))
	numlit.remove(max(numlit))