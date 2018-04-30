dtuple=(('a'),('b')),(('c'),('d'))

def func(tup):
    return list(map(lambda x,y:dict(zip(x,y)),tup[0],tup[1]))  

print(func(dtuple))
