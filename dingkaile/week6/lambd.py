y=lambda a: {a[0]:a[1]}
tmp=[]
for i in ((('a'),('b')),(('c'),('d'))):
	tmp.append(y(i))

print(tmp)