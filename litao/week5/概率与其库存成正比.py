# 已知仓库中有若干商品，以及相应库存，类似：
# 袜子，10
# 鞋子，20
# 拖鞋，30
# 项链，40
# 要求随机返回一种商品，要求商品被返回的概率与其库存成正比。请描述实现的思路或者直接写一个实现的函数

import random

commo_dict = {'wazi': 10, 'xiezi': 20, 'tuoxie': 30, 'xianglian': 40}


def randcommo(commo):
    commo_list = []
    for i in commo.keys():
        commo_list.extend([i] * commo[i])
    print(random.choice(commo_list))


randcommo(commo_dict)
# def commodity(rand_com):