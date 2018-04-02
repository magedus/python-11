feb = [1,1]
n = 1
while feb[-1] < 100:
    feb.append(feb[n] + feb[n-1])
    n = n + 1
feb.pop(-1)
print(feb)
