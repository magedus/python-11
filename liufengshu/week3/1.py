lst = ['a', 'b', 'c']
lst1 = ['a','b','c','d','e']
def find_x(x, lst):
    return True if x in lst else False

for x in lst1:
    print(x,find_x(x, lst))