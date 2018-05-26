#!/usr/bin/env python
# -*- coding: utf-8 -*-

def new_counter(num: int):
    """
    
    请实现函数 new_counter ，使得调用结果如下：
    c1 = new_counter(10)
    c2 = new_counter(20)
    print（c1(), c2(), c1(), c2()）

    outputs ：
    11 21 12 22
    """
    
    def _inner():
        nonlocal num
        num += 1
        return num
    return _inner


c1 = new_counter(10)
c2 = new_counter(20)
print(c1(), c2(), c1(), c2())
