start=0
step=1
result=0
flag=0
while not flag:
	if result < 100:
		print(result)
		flag=0
		result = start + step
		start = step
		step = result
	else:
		flag=1
