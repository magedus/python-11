lst = [0,1]

while lst[-1] < 100:
    cur = lst[len(lst)-2] + lst[len(lst)-1]
    lst.append(cur)
print(lst)
