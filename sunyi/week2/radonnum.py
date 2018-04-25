import time
import hashlib

radonnum = []
index = 0
# 生成md5对象
radon = hashlib.md5()
for index in range(200):
    # 设置一个基数，由时间获取
    base = str(time.time())
    #生成随机数
    radon.update(base.encode(encoding='utf-8'))
    radonnum.append ( radon.hexdigest())
    print(radonnum[index])
    print()
    index += 1

