

print((lambda i,j:[{i[0]:j[0],j[0]:j[1]}])((('a'),('b')),(('c'),('d'))))   #dest is [{'a':'c'｝,{'c':'d'}]

print((lambda i,j:[dict(zip(i,j))])((('a'),('b')),(('c'),('d'))))   #dest is [{'a': 'c', 'b': 'd'}]