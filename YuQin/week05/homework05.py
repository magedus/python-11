#打乱列表
import random

alist=[1,2,3,4,5]
random.shuffle(alist)
print(alist)

#随机返回一种商品
store=["袜子"]*10 + ["鞋子"]*20 + ["拖鞋"]*30 + ["项链"]*40
random.shuffle(store)
target=random.choice(store)
print(target)
