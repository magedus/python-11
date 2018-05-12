srclst = [1,5,2,7,4,9]

def cal_num1_num2(sum,srclst):
    lst = []
    for i in range(len(srclst) - 1):
        x = srclst[i]
        for j in range(i + 1, len(srclst)):
            y = srclst[j]
            if sum == x + y:
                lst.append((x,y))

    return lst

print(cal_num1_num2(9,srclst))

