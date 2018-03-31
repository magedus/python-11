###2、打印出100以内的斐波那契数列，使用2种方法实现###
################1#################
a = 1
b = 1
c = 0
lst1 = []
lst1.append(a)
lst1.append(b)
while True:
    c = a + b
    if c>=100:
        break
    else:
        lst1.append(c)
        a = b
        b = c
print("Way 1: ",lst1)
#################2###################
lst2 = [1,1]
while True:
    lst_len = len(lst2)
    new_num = lst1[lst_len - 1] + lst1[lst_len - 2]
    if  new_num >=100:
        break
    else:
        lst2.append(new_num)
print("Way 2: ",lst2)
