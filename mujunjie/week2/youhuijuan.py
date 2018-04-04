import random
a = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
b = set()
for i in range(200):
    b.add("".join(random.sample(a,5)))
print(list(b))

