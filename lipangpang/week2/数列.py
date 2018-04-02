print ([x[0] for x in [ (a[i][0], a.append((a[i][1], a[i][0]+a[i][1]))) for a in ([[1,1]], ) for i in range(100) ]])

f = lambda x,y,n:x if not n else f(y,x+y,n-1)
print(list(map(lambda n:f(1,1,n),range(100))))