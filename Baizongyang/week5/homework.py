#打乱一个排好序的列表
import random
def shuffleList(*iterable):
    lst = []
    [ lst.append(i) for i in iterable ]
    random.shuffle(lst)
    print(lst)

shuffleList(*[1,2,3,4,5])



#返回商品的问题还没有写出来，在此写下我的思路：
    #四种商品的比例是1:2:3:4
    #抽象成一个列表['A','B','B','C','C','C','D','D','D','D']
    #将逻辑写成一个函数，有一个形参是控制调用次数，默认值为1，即调用一次
    #核心逻辑就是根据调用的次数（假设这个次数为count），计算出四种商品的库存比例和调用次数count的关系，根据这个关系返回对应的商品。这块没想好怎么实现。
