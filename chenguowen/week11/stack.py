#!/usr/bin/env python
# -*- coding: utf-8 -*- 

"""
    实现数据结构stack(栈)，并实现它的append，pop方法【动手查询相关资料理解stack特点以及与queue区别】
    stack：后进先出
    queue: 先进先出

"""

class Stack(object):
    def __init__(self):
        self.items = []

    # append
    def push(self,item):
        self.items.append(item)

    # pop
    def pop(self):
        if self.items:
            return self.items.pop()
        else:
            print('Stack is empty!')

stack = Stack()

# 压栈
stack.push('Hello')
stack.push('Python')


# 出栈
print(stack.pop())
print(stack.pop())
