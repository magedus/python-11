import random
import collections

# inventory initialization
inv = {'sock': 10, 'shoe':20,'slipper':30,'necklace':40}


def sampling(inv):
    
    pro_smp= collections.OrderedDict()
    n = len(inv)
    total = 0
  
    sub=[]
    for v in inv.values():
        total += v
        sub.append(total)
    
    i=0
    for k in inv.keys():
        pro_smp[k] = sub[i]/total
        i += 1
    
    draw = random.random()
    print(draw)
    print(pro_smp)
    
    for k,v in pro_smp.items(): 
        if draw < v : 
            print("reult:",k,v)
            break
        
        
sampling(inv)
    





        
    
