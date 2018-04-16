from  pathlib import Path
import re
p = Path('english.txt')

with open(p.absolute(), 'r') as f:

    r = f.read().replace(".","")
    word_list= re.split("[\?\"\,\s]+", r)
    print(len(word_list))
