import random

for _ in range(200):
    print(''.join([chr(random.randint(97,122)) for i in range(6)]))
