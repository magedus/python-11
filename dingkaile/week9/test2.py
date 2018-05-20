flag =  False
def repeat(string):
	global flag
	for i in string:
		if i.isalpha and string.count(i)>1:
			flag=True
			break

str1=input('input a string ')
repeat(str1)
if flag:
	print('string has repeated')
else:
	print('the string has no repeated')