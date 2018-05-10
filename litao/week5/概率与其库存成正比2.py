import random

commo_dict = {'wazi':10,'xiezi':20,'tuoxie':30,'xianglian':40}
commo_list = []
[commo_list.extend([i]*commo_dict[i]) for i in commo_dict.keys()]
print(random.choice(commo_list))