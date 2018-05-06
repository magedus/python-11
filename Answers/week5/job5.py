import random

# 1、打乱一个排好序的list对象alist，alist=[1,2,3,4,5]

alist = [1, 2, 3, 4, 5]


def randmon_list(lst: list) -> list:
    random.shuffle(lst)
    return lst

# 2、已知仓库中有若干商品，以及相应库存，类似：
# 袜子，10
# 鞋子，20
# 拖鞋，30
# 项链，40
# 要求随机返回一种商品，要求商品被返回的概率与其库存成正比。请描述实现的思路或者直接写一个实现的函数


def get_product():
    sock_lst = ['socke'] * 10
    shoe_lst = ['shoe'] * 20
    t_shoe_lst = ['t_shoe'] * 30
    necklace_lst = ['necklace'] * 40
    products_lst = shoe_lst + sock_lst + t_shoe_lst + necklace_lst
    return random.choice(products_lst)



