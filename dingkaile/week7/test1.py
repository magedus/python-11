a="1,2,3"
print(a)
b=[]
for i in a:
	if i.isalnum():
		b.append(i)
print(b)