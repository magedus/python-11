"""实现函数 new_counter ，使得调用结果如下：
c1 = new_counter(10)
c2 = new_counter(20)
print（c1(), c2(), c1(), c2()）
outputs ：
11 21 12 22"""

def new_counter(number):
    init_number = {number:number}
    def _new_counter():
        init_number[number] += 1
        return init_number[number]
    return _new_counter

c1 = new_counter(10)
c2 = new_counter(20)

print(c1(),c2(),c1(),c2())