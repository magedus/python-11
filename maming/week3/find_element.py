def find_element(*alnum,x=11):
    if x in alnum:
        print("find it!")
        return 1
    else:
        print("Can't find!")
        return 0

find_element(1,2,3,4,3,4,13,2123,231,31,23,1,2132,1,9)
    
