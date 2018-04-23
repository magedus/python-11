import random

"""
打乱一个排好序的list对象alist，alist=[1,2,3,4,5]
"""


def disorder_list(lst: list):
    random.shuffle(lst)
    return print(lst)


alist = [1, 2, 3, 4, 5]
disorder_list(alist)


"""
2、已知仓库中有若干商品，以及相应库存，类似：
袜子，10
鞋子，20
拖鞋，30
项链，40
要求随机返回一种商品，要求商品被返回的概率与其库存成正比。请描述实现的思路或者直接写一个实现的函数 
温馨提示：请在4月23日前完成
"""


def show_goods(dt: dict):
    dt2 = {v: k for k, v in dt.items()}
    keys = dt2.keys()
    lit = []
    for key in keys:
        for i in range(key):
            lit.append(dt2[key])
    return lit[random.randint(0,len(lit)-1)]


dt = {'shoes': 20, 'flats': 30, 'socks': 10, 'rings': 40}
print(show_goods(dt))

