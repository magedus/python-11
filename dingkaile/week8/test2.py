lst=input('input a int list ')
tmp=[]
for i in lst:
	if i.isdigit():
		tmp.append(int(i))
sumn=int(input('input a sum'))
print(tmp)
a=set()
for i in tmp:
	i = int(i)
	j=sumn - i
	if j in tmp:
		print(i,j)
		tmp.remove(i)

	

