# -*- coding: UTF-8 -*-
# lambda

t1 = (('a'), ('c'))
t2 = (('b'), ('d'))

print(list(map(lambda t: {t[0]: t[1]}, zip(t1, t2))))

l = lambda t1, t2: [{i: j} for i, j in zip(t1, t2)]
print(l(t1, t2))