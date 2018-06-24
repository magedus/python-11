
def tosentense(string,onedict):
	tmp=[]
	point=0
	for i in range(point,len(string)):
		if string[point:i+1] in onedict:
			tmp.append(string[point:i+1])
			point=i+1
	print(' '.join(tmp))

tosentense('thisisanexample',['is','this','an','example'])