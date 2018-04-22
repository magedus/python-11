# -*- coding: UTF-8 -*-
"""
2、已知仓库中有若干商品，以及相应库存，类似：
袜子，10
鞋子，20
拖鞋，30
项链，40
要求随机返回一种商品，要求商品被返回的概率与其库存成正比。请描述实现的思路或者直接写一个实现的函数 
"""
import random


warehouse = {'sock': 10, 'shoes': 20, 'slippers': 30, 'necklace': 40}


# 方法一
def commodity_probabilities(warehouse):
    probabilities = {}
    warehouse_count = 0
    for i in warehouse:
        warehouse_count += warehouse[i]
    for m in warehouse:
        probabilities[m] = warehouse[m] / warehouse_count
    return probabilities
    

def random_return_commodity1(probabilities):
    x = random.choice(range(1, 100)) / 100
    #print(x)
    scale = []
    probabilities_rev = {}
    for k, v in probabilities.items():
        probabilities_rev[v] = k
        scale.append(v)
    scale.sort()
    #print(scale)
    #print(probabilities_rev)
    for i in range(len(scale)):
        if i == len(scale) - 1:
            break
        #print(scale[i])
        if x <= scale[0]:
            print(probabilities_rev[scale[0]])
            break 
        if scale[i] < x <= scale[i+1]:
            print(probabilities_rev[scale[i+1]])
            break       
        if x > scale[-1]:
            print(probabilities_rev[scale[-1]])
            break
    
    
random_return_commodity1(commodity_probabilities(warehouse))

#方法二
def random_return_commodity2(warehouse):
    probabilites = []
    for k, v in warehouse.items():
        probabilites += [k] * v
    random.shuffle(probabilites)
    
    print(random.choice(probabilites))


#random_return_commodity2(warehouse)

        





