start=0
step=1
result=0
while result < 100:
	result = start + step
	start = step
	step = result
	if result < 100:
		print(result)
