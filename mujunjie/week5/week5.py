#1打乱一个排好序的list对象alist，alist=[1,2,3,4,5]
import random
alist = [1,2,3,4,5]

def shufle(lst):
    random.shuffle(lst)
    return lst

print(shufle(alist))

'''2 已知仓库中有若干商品，以及相应库存，类似:
袜子 20
鞋子 20
项链 30
拖鞋 40
'''
'''a ,b ,c ,d 分别对应以上袜子，鞋子，项链，拖鞋'''

def rand():
    a = int(20/((20+20+30+40))*100)   #算出所有商品比例
    b = int(20/((20+20+30+40))*100)
    c = int(30/((20+20+30+40))*100)
    d = int(40/((20+20+30+40))*100)
    f = random.randint(1,100)
    print(f)
    if f < a:                         #随机生成1-100的数，当商品比例数值大于生成的随机数是，返回该商品
        print("{}".format("袜子"))    #返回A
    elif f < (a+b):
        print("{}".format("鞋子"))    #返回B
    elif f < (a+b+c):
        print("{}".format("项链"))    #返回C
    else:
        print("{}".format("拖鞋"))    #返回D

rand() 
