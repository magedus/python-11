import random

stock = {}

socks = dict(map(lambda i:(i,'socks'),range(1,11)))
stock.update(socks)
shoes = dict(map(lambda i:(i,'shoes'),range(11,31)))
stock.update(shoes)
slippers = dict(map(lambda i:(i,'slippers'),range(31,61)))
stock.update(slippers)
necklace = dict(map(lambda i:(i,'necklace'),range(61,101)))
stock.update(necklace)
#print(stock)

k = random.choice([i for i in range(1,101)])
print(stock[k])