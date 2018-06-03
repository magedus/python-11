# 现有两元祖 (('a'),('b')),(('c'),('d')) ,请使用Python中的匿名函数生成列表 [ {'a':'c'｝,{'b':'d'}]
# 列表解析式+lambda函数返回的表达式值
t1, t2 = (('a'), ('b')), (('c'), ('d'))
x = [(lambda k,v:{k:v})(k,v) for k,v in zip(t1,t2)]
print(x)


