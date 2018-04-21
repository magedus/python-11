import  random

goodsDic={
      'socks':10
      ,'shoes':20
      ,'slippers':30
      ,'necklace':40
}

def randomGoods(goods):
      goodsList=[]
      for k,v in goods.items():
            goodsList+=[k]*int(v)
      return random.choice(goodsList)

print(randomGoods(goodsDic))

