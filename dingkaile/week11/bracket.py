
def bracket(n,left,right,couple):
	if left == 0 and right == 0:
		print(couple)
	else:
		if left > 0:
			bracket(n,left-1,right,couple+'(')
		if left < right:
			bracket(n,left,right-1,couple+')')
bracket(3,3,3,'')