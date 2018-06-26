
def findmaxlist(Lst):
	tmplist=sorted(Lst)
	t=[]
	for i in range(0,len(tmplist)-1):
		var = tmplist[i+1]-tmplist[i]
		t.append(tmplist[i])
		if var != 1:
			t.append(',')
	t.append(tmplist[i+1])
	t.append(',')
	return t

tmp=[]
result=[]
for i in findmaxlist([4,6,8,3,1,10,19,45,47,46,50,53,52,51]):
	if i != ',':
		tmp.append(i)
	else:
		result.append((tmp,len(tmp)))
		tmp=[]		

maxl=0
for i in result:
	if maxl < i[1]:
		maxl=i[1]
		tu=i
print(tu)