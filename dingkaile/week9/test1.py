def new_counter(a):	
	def addstep():
		nonlocal a
		a+=1
		return a
	return addstep

c1 = new_counter(10)
c2 = new_counter(20)
print(c1(),c2(),c1(),c2())