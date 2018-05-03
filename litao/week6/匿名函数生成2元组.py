#现有两元祖 (('a'),('b')),(('c'),('d')) ,请使用Python中的匿名函数生成列表 [ {'a':'c'｝,{'b':'d'}]
tup = (('a'),('b')),(('c'),('d'))
print((lambda x:[{v:k} for k,v in zip(x[1:][0],x[:1][0])])(tup))
