# Solution 1
import random
len_SN = 10
num_SN = 200
dic_SN = list(range(48, 58)) + list(range(65, 91)) + list(range(97, 123))
for i in range(len(dic_SN)):
    dic_SN[i] = chr(dic_SN[i])
SN = ''
SNs = []
for j in range(num_SN):
    for i in range(len_SN):
        SN += random.choice(dic_SN)
    if SN not in SNs:
        SNs.append(SN)
    SN = ''
print(SNs)

# Solution 2
import random
len_SN = 10
num_SN = 200
dic_SN = list(range(48, 58)) + list(range(65, 91)) + list(range(97, 123))
for i in range(len(dic_SN)):
    dic_SN[i] = chr(dic_SN[i])
SNs = []
for j in range(num_SN):
    SN = "".join(random.choices(dic_SN, k=10))
    if SN not in SNs:
        SNs.append(SN)
print(SNs)
