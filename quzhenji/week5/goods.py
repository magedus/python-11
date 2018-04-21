import random


Socks = ['Sock']*10
shoes = ['shoes']*20
Slipper = ['Slipper']*30
Necklace = ['Necklace']*40

all_goods = Socks + shoes + Slipper + Necklace

print(all_goods)
print('*'*200)
print(random.choice(all_goods))