import random
num_lst = []*20
for i in range(20):
    num_lst.append(random.choice(range(100)))
num_lst.sort(reverse=True)
print(num_lst[0], num_lst[1], num_lst[2])
