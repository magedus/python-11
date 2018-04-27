
#斐波那契数列
f0 = 1
f1 = 1
fn = 0
print(f0)
print(f1)
while True:
    fn = f0 + f1
    f0 = f1
    f1 = fn
    if fn > 100:
        break
    print(fn)