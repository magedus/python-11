lit=list(input('input a list:'))
key=input('input a argument:')
def findaugument(key,lit):
	if key in lit:
		return 1
	else:
		return 0

print(findaugument(key,lit))