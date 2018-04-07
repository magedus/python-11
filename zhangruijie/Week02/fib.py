#Method 1:

fib=[0,1]
i=1
while fib[i-1]+fib[i]<=100:
    fib.append(fib[i-1]+fib[i])
    i += 1
print(fib)

#Method 2：
fibonacci=[]
for i in range(100):
	if i+1 <= 2:       			#	setting first 2 items 
		fibonacci.append(i)
	else:						#	generate next item with rule
		fibonacci.append(fibonacci[i-1]+fibonacci[i-2])
	
	if fibonacci[i]>= 100:		#	 > 100 ? stop
		fibonacci.pop(i)
		break
print(fibonacci)
