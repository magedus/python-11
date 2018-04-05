import string
import random
code_list = []
i = 0
while i < 200:
    code =''.join(random.sample(string.ascii_letters+string.digits,5))
    if code not in code_list:
        code_list.append(code)
        i= i + 1
for j in range(200):
    print("第",j+1,"个优惠券是：",code_list[j])