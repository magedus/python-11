import random

goodsDic={
      'socks':10
      ,'shoes':20
      ,'slippers':30
      ,'necklace':40
}

goodsList=[]
for k in goodsDic:
      for i in range(goodsDic[k]):
            goodsList.append(k)

print(random.choice(goodsList))