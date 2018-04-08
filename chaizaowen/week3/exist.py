def exist(*args):
    if 'x' in args:
        return 1
    else:
        return 0

print(exist(*[1,2,3,4,'x']))