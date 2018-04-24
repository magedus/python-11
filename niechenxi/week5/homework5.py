#作业1：打乱一个排好序的list对象alist，alist = [1,2,3,4,5]
#作业2：已知仓库中有若干商品，以及相应库存，类似：
#       袜子，10
#       鞋子，20
#       拖鞋，30
#       项链，40
#       要求随机返回一种商品，要求商品被返回的概率与其库存成正比。请描述实现的思路或者直接写一个实现的函数


#作业一：
import random
alist = [1,2,3,4,5]
newlist = []
while alist:
    element = random.choice(range(len(alist)))
    newlist.append(alist[element])
    alist.remove(alist[element])
print(newlist)




#作业二:
import random
def popgoods():
    goodsdict = {40:'necklace', 30:'slippers', 20:'shoes', 10:'secks'}
    goodslist = []
    
    #变量字典，把对应的个数append进列表中
    for k,v in goodsdict.items():
        for _ in range(0,k//10):
            goodslist.append(v)
    return goodslist[random.choice(range(len(goodslist)))]

good = popgoods()
print(good)
