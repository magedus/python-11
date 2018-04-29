import random

def getproduct(index):
	if index == 1:
		return "socks"
	elif index in [2,3]:
		return "shoes"
	elif index in [4,5,6]:
		return "slippers"
	else:
		return "necklace"
A1=0
A2=0
A3=0
A4=0
for i in range(0,10000):
	index=random.randint(1,10)
	j=getproduct(index)
	if j == "socks":
		A1+=1
	elif j == "shoes":
		A2+=1
	elif j == "slippers":
		A3+=1
	else:
		A4+=1
print(A1,A2,A3,A4)