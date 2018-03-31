lst1 = [0,1]
print(lst1[0])
print(lst1[1])
for i in range(2,100):
    temp = lst1[i-2] + lst1[i-1]
    lst1.append(temp)
    print(lst1[i])