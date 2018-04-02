feb = []
a = 1
b = 0
while a < 100:
    feb.append(a)
    a = a + b
    b = feb[-1]
print(feb)