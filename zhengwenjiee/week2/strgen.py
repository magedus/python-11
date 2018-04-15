"""
    String Generation
    -----------------
    The important THING is(英語去重怎麼説) 
"""

import string
import random
    
class StrGen(object):
    
    def strgen1(self, size, nums):
        seq = []
        char = string.ascii_uppercase + string.digits
        while len(seq) != nums:
            strs = ''.join(random.choices(char, k=size))
            if strs not in seq:       
                seq.append(strs)

        return seq
    
    def strgen2(self, size, nums):
        seq = set()
        char = string.ascii_uppercase + string.digits
        while len(seq) !=nums:
            strs = ''.join(random.choices(char, k=size))
            seq.add(strs)

        return list(seq)  
    
strgen = StrGen()
s = strgen.strgen1(6, 10)
for i in s:
    print(i)
