def findlocation(str1,str2):
	if str2 in str1:
		return(str1.find(str2))
	else:
		return(None)

str1=input('input str1 ')
str2=input('input str2 ')

a=findlocation(str1,str2)
print(a)