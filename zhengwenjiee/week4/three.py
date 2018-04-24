import random

lst =random.sample(range(100), k=20) 

def three(lst=None):
    if lst != None:
        lsted = sorted(lst, reverse=True)
        return lsted[:3]
          
three(lst=lst)