import random
result = [random.randint(1,100) for i in range(19)]
print result
result1 = sorted(result)
print result1[-1],result1[-2],result1[-3]