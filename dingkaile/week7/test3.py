li = [[]]*5  # copy [] 5 times,not deep copy
li[0].append(10)
print(li)
li[1].append(20)  #id(li[0]),id(li[1])...id(li[4]) are the same
print(li)
li.append(30) # li append
print(li)
