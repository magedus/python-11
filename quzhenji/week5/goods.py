import random

def goods():
    Socks = ['Sock']*10
    shoes = ['shoes']*20
    Slipper = ['Slipper']*30
    Necklace = ['Necklace']*40

    all_goods = Socks + shoes + Slipper + Necklace
    random.shuffle(all_goods)

    return random.choice(all_goods)

dict1 = {}
goods_lst = []
for _ in range(100):
    goods_lst.append(goods())

#print(goods_lst.count("Sock"))
for _ in range(4):
    dict1['Sock'] = goods_lst.count("Sock")
    dict1['shoes'] = goods_lst.count("shoes")
    dict1['Slipper'] = goods_lst.count("Slipper")
    dict1['Necklace'] = goods_lst.count("Necklace")

print(dict1)