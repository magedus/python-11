#随机生成20个数字，并且筛选出其中最大的3个数
import random

rand_list = [random.randint(1,1000) for _ in range(20)]
rand_list_new = sorted(rand_list)

print('Max number is {}.\nSecond number is {}.\nThird number is {}.'.format(rand_list_new[-1],rand_list_new[-2],rand_list_new[-3]))