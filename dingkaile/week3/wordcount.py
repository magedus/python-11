filename='file.txt'

f=open(filename,'r')

word=[]
tmp=f.read().split()
f.close()

for i in tmp:
	i=i.lower().strip(',.!#?: ')
	if i not in word:
		word.append(i)
#print(word)

fileword=[]
for i in tmp:
	i=i.lower().strip(',.!#?: ')
	fileword.append(i)

for i in word:
	print(i + " occurs " +str(fileword.count(i)) + ' times')