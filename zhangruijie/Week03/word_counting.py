
f = open('/home/python/ga.txt')
raw_contents = f.read()
f.close
# 不仅要考虑空格，还要去掉文中的 ，. ；
#contents=raw_contents.split()
contents=raw_contents.replace(',','').replace(';','').replace('.','').split()
l = len(contents)
s = set(contents)
n = len(s)
print("there are %d words in the Gettysburg Address,as well as %d different words" % (l,n))

# calculate words frequency ... 
freq ={}

for w in contents:
	if w not in freq:
		freq[w] = 1
	else :
		freq[w] += 1

print(sorted(freq.items()))

		

		
	