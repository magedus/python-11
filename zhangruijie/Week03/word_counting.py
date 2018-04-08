
f = open('/home/python/ga.txt')
raw_contents = f.read()
f.close
contents=raw_contents.split()
l = len(contents)
s = set(contents)
n = len(s)
print("there are %d words in the Gettysburg Address,as well as %d different words" % (l,n))

# calculate words frequency ... 
d = dict.fromkeys(contents,0)

# after finish learning dict function 
		
	