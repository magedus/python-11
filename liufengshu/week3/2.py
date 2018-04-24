from  pathlib import Path
import re
p = Path('english.txt')

with open(p.absolute(), 'r') as f:

    result = re.findall('[a-zA-Z]+(?:[\'\’])?[a-zA-Z]*',f.read())

d ={}
for word in result:
    if word in d:
        d[word] += 1
    else:
        d[word]  = 1
print(d)

print(len(result))

