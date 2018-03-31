import random
key = list(map(chr, range(ord('a'), ord('z') + 1)))
old_key =[(0,0,0,0,0)]*200
for i in range(200):
    b = random.sample(key,5)
    if b in old_key:
        continue
    old_key[i] = b
    print('第{}个优惠券：{}{}{}{}{}'.format(i+1,b[1],b[2],b[3],b[0],b[4]))