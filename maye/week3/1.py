'''
    import random
    lst=[[1,2,3],["x",7,8],[9,6]]
    lst1=random.choice(lst)
    if 'x' in lst1:
        print(lst1)
        print("存在",1)
    else:
        print(lst1)
        print("不存在",0)
    '''

str1="After final machining, all surfaces shall be examined by the wet magnetic particle method in accordance with ASME VIII, Division 1, Appendix 7.    If magnetic particle examination is not possible, then liquid penetrant examination shall be performed in accordance with ASME VIII, Division 1, Appendix 7.    6.13.2.4          Replace this clause with:   Nodular iron castings shall be produced in accordance with ASTM A395/A395M, or ASTM A536/A536M provided it meets or exceeds the material requirements of ASTM A395 as indicated by appropriate testing"
str2=str1.split()
print(str2.count("in"))
