import random
result=[]
Length=0
counter=0
while counter<200:
	String=[]
	Length=random.randint(5,11)
	for j in range(0,Length+1):
		k = random.randint(0,3)
		if k == 0:
			l=random.randint(ord('a'),ord('z'))
		elif k == 1:
			l=random.randint(ord('A'),ord('Z'))
		else:
			l=random.randint(ord('0'),ord('9'))
		if chr(l) not in String:
			String.append(chr(l))
	String=''.join(String)
	if len(String) >= 5:
		result.insert(counter,String)
		counter+=1
for i in result:
	print(i)




