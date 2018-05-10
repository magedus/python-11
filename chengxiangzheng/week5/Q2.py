#要求随机返回一种商品,要求商品被返回的概率与其库存成正比。
import random  
wazi=['wazi'] * 100  
xiezi=['xiezi'] * 200  
tuoxie=['tuoxie'] * 300  
xianglian=['xianglian'] * 400  
s1= wazi+xiezi+tuoxie+xianglian  
s2 = random.sample(s1,100) 
#print(s1)
#print(s2)
print(s2.count('wazi'),end=" ")     #count()方法用于统计某个元素在列表中出现的次数。
print(s2.count('xiezi'),end=" ") 
print(s2.count('tuoxie'),end=" ")  
print(s2.count('xianglian')) 