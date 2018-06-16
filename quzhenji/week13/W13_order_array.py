
def findKthfromTwoarray(lst1,lst2,k):
    lst3 = []
    lst3.extend(lst1)
    lst3.extend(lst2)
    sorted(lst3)
    return lst3[k]

lst1 = [1,2,3,4]

lst2 = [10,15,16,21,25]

result = findKthfromTwoarray(lst1, lst2, 7)
print(result)

