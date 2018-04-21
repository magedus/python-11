import random


activation = set()
while True:
    if len(activation) == 200:
        break
    else:
        activation.add(random.choice(range(10000, 99999)))


for i in activation:
    print(i)
