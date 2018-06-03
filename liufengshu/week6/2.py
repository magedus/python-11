set1 = (('a'),('b')) # ('a', 'b')
set2 = (('c'),('d')) # ('c', 'd')
set3 = (('e'),('f'))


L = (lambda *args:[{k:v} for k,v in args])(set1, set2, set3)
print(L)


