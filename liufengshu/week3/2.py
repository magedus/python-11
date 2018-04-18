from  pathlib import Path
import re
p = Path('english.txt')

with open(p.absolute(), 'r') as f:

    result = re.findall('[a-zA-Z]+(?:\'|\¡¯)?[a-zA-Z]*',f.read())

print(result)
print(len(result))
