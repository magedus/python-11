print('please input three integer')
x = int(input())
y = int(input())
z = int(input())
if x > y:
    if z<y:print(z,y,x)
    else:
        if x>z:print(y,z,x)
        else:print(y,x,z)
else:
    if x>z:print(z,x,y)
    else:
        if y>z:print(x,z,y)
        else:print(x,y,z)
