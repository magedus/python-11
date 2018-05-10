"""已知仓库中有若干商品，以及相应库存，类似：
袜子，10
鞋子，20
拖鞋，30
项链，40
要求随机返回一种商品，要求商品被返回的概率与其库存成正比。请描述实现的思路或者直接写一个实现的函数
"""
# 计算商品的总数，利用random生成随机数，看其落在商品总数的哪一个区段，返回对应商品
import random


def recommend(socks=10, shoes=20, slipper=30, necklace=40):
    all_num = socks + shoes + slipper + necklace
    y = (random.randint(1, all_num) for random.randint(1, all_num) in range(1, all_num))
    random_num = next(y)
    """调试
    print(random_num)
    print("<", socks+1,random_num in range(1, socks+1))
    print(socks + 1, "<", socks + shoes + 1, random_num in(socks + 1, socks + shoes + 1))
    print(socks + shoes + 1, "<", socks + shoes + slipper + 1, random_num in (socks + shoes + 1, socks + shoes + slipper + 1))
    print(socks + shoes + slipper + 1, "<", all_num + 1, random_num in (socks + shoes + slipper + 1, all_num + 1))
    """
    if random_num in range(1, socks+1):
        return "socks"
    if random_num in range(socks + 1, socks + shoes + 1):
        return "shoes"
    if random_num in range(socks + shoes + 1, socks + shoes + slipper + 1):
        return "slipper"
    if random_num in range(socks + shoes + slipper + 1, all_num + 1):
        return "necklace"


# 测试比例是否大致相同
"""
def testmore(times,socks = 10, shoes = 20, slipper = 30, necklace = 40):
    test_socks = 0
    test_shoes = 0
    test_slipper = 0
    test_necklace = 0
    all_num = socks + shoes + slipper + necklace
    for test in range(1,times+1):
        test_result = recommend(socks,shoes,slipper,necklace)
        if test_result == "socks":
            test_socks += 1
        elif test_result == "shoes":
            test_shoes += 1
        elif test_result == "slipper":
            test_slipper += 1
        elif test_result == "necklace":
            test_necklace += 1
    print("test %d times",%times)
    print("test socks:", test_socks, test_socks / times)
    print("test shoes:", test_shoes, test_shoes / times)
    print("test slipper:", test_slipper, test_slipper / times)
    print("test necklace:", test_necklace, test_necklace / times)
"""


a = recommend()
print(a)
# testmore(10000, 10, 20, 30, 40)
