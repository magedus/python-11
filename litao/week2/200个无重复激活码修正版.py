import random

key = list(map(chr, range(ord('a'), ord('z') + 1)))
old_key =[0]*200 #保存之前存在的优惠券
count = 0 #统计优惠券个数

while True:
    b = random.sample(key,5)
    if b in old_key:
        continue
    old_key[count] = b
    print('第{:03}个优惠券: {}'.format(count+1,''.join(b)))
    count += 1
    if count == 200:
        break