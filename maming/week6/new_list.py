dtuple=(('a'),('b')),(('c'),('d'))

def func(tup):
    return list(map(lambda x,y:dict(zip(x,y)),*tup))  

print(func(dtuple))
