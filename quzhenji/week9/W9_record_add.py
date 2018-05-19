def new_counter(num:int)->int:
    ret = num
    def _new_counter():
        nonlocal ret
        ret += 1
        return ret
    return _new_counter

c1 = new_counter(10)
c2 = new_counter(20)
print(c1(),c2(),c1(),c2())