import random
#'a' 代表袜子 'b'鞋子 'c'拖鞋 'd'项链
goods = []
goods = ['a']*10 + ['b']*20 + ['c']*30 + ['d']*40  		
goods_dict = {'a':'袜子','b':'鞋子','c':'拖鞋','d':'项链'}

print(goods_dict.get(random.choice(goods)))