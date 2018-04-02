# 100以内的斐波那契数列
# 方法1：
print(1)
a = 0
b = 1
for i in range(101):
    c = a + b
    if c > 100:
        break
    a = b
    b = c
    print(c)

# 方法2：
print(1)
a = 0
b = 1
while True:
    c = a + b
    if c > 100:
        break
    a = b
    b = c
    print(c)

#