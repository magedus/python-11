#!/usr/bin/env python
# -*- coding: utf-8 -*-

def foo(output,open,close,pairs):
    """

    打印出N对合理的括号组合。
    例如： 当N=3，输出：()()(),()(()),(())(),((()))
    """

    if open == pairs and close == pairs:
        print(output)
    else:
        if open < pairs:
            foo(output+'(',open+1,close,pairs)

        if close < open:
            foo(output+')',open,close+1,pairs)

foo('', 0, 0, 3)
