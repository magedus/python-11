#########200 无重复激活码（或者优惠券），字符串长度大于5以上####
import random
Num_lst = []
Upp_lst = []
Low_lst = []
Quit_cmd = 'quit'
for i in range(48,58):
    Num_lst.append(i)
for j in range(65,91):
    Upp_lst.append(j)
for m in range(97,123):
    Low_lst.append(m)

while True:
    R_Count = input("Input length(must be more than 5) or quit : ")
    if R_Count == Quit_cmd:
        break
    elif  R_Count.isdigit() and int(R_Count) > 5:
        New_lst = set()
        while len(New_lst)<200:
            T_set = []
            for _ in range(int(R_Count)):
                T_set.append(chr(random.choice(Num_lst + Upp_lst + Low_lst)))
            New_lst.add(''.join(T_set))
        print(New_lst)
    else:
        continue
