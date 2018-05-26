from random import choice, randrange

d = {'a':10,
     'b':20,
     'c':30,
     'd':40
     }

# dict to list
def d_to_lst(d:dict):
    lst = []
    for k,v in d.items():
        lst += [k]*v
    return lst

# 随机挑选一个
def random_selectone(l:list):
    return choice(l)

# 随机挑选list长度个，
def random_selectall(l:list):
    d = {}
    for i in range(len(l)):
        temp = l[randrange(len(l))]
        if not d.get(temp):
            d[temp] = 1
        else:
            d[temp] += 1
    return d

print(random_selectone(d_to_lst(d)))
print(random_selectall(d_to_lst(d)))
