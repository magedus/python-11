import random
get_lst = [random.randrange(1, 10000) for x in range(0, 20)]
print("random num is :",get_lst)
# 排序，切片取最后三个即为最大的三个
get_lst.sort()
print("max 3 num is :",get_lst[-4:-1:])