lst=[1,1]
for i in range(2,20):
    print(lst)
    if lst[i-1] + lst[i-2] > 100:
        break
    lst.append(lst[i-1] + lst[i-2])
print(lst)