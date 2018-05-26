def new_counter(a:int):
    b = [a]
    def inc():
        b[0] += 1
        return b[0]
    return inc

c1 = new_counter(10)
c2 = new_counter(20)
print(c1(),c2(),c1(),c2())