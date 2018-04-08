	
import random
raw="abcdefghijklmnopqrstuvwxwz"
lst=list()
for _ in range(50):
	lst += raw[random.randint(0,25)]

print(lst)
counter = 0
for c in lst :
    if c =="x":
        
        counter += 1
    
if counter == 0:
    print("there is no 'x' is in the string")
elif counter == 1:
    print("there is 1 'x' in the string")
else:
    print("there are %d 'x' in the string" % counter)