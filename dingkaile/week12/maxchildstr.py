Str=input('input a string: ')

def maxchildstr(String):
	tmp=[]
	lst=[]
	length=len(String)
	for i in range(0,length):
		for j in range(i,length):
			if String[j] not in tmp:
				tmp.append(String[j])
			else:
				lst.append(''.join(tmp))
				tmp=[]
				break
	#print(lst)
	Len=0
	word=''
	for i in lst:
		if Len < len(i):
			Len=len(i)
			word=i
	print(word)
	return word 
maxchildstr(Str)

