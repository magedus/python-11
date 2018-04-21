import random
lst = [random.randint(1,1000) for _ in range(20)]
max =[lst[0],lst[0],lst[0]]
print(lst)

for i in range(20):
    if lst[i] > max[0]:
        max[2],max[1],max[0] = max[1],max[0],lst[i]
    elif lst[i] > max[1]:
        max[2],max[1] = max[1],lst[i]
    elif lst[i] > max[2]:
        max[2] = lst[i]

print(max)
