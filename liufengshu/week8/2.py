import copy
def sum_for_two_int(lst:list,sum:int):
    lst = copy.copy(lst)
    result = []
    for i in lst:
        if sum-i in lst:
            result.append((i, sum-i))
            lst.remove(i)
            lst.remove(sum-i)
    return result

if __name__ == '__main__':
    lst = [1,2,3,4,5,6,7,8,9]
    result = sum_for_two_int(lst, 8)
    print(result)
    print(lst)


