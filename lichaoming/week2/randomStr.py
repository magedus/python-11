import random
import string

#长度为8的字符串随机数
str_length = 8
for i in range(200):
    random_str = ''.join(random.sample(string.ascii_letters + string.digits , str_length))
    print(random_str)