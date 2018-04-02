num1 = 0
num2 = 1
if num1 == 0:
    print(1)
while True:
    total = num1 + num2
    num1 = num2
    num2 = total
    if total >= 100:
        break
    print(total)