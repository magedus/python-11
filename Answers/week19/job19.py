# 1、使用Python实现一个双端队列


class Deque:
    def __init__(self):
        self.items = []


    def is_empty(self):
        return self.items == []


    def add_front(self, item):
        self.items.append(item)


    def add_rear(self, item):
        self.items.insert(0, item)


    def remove_front(self):
        return self.items.pop()


    def remove_rear(self):
        return self.items.pop(0)


    def size(self):
        return len(self.items)

# 2、输入n 个整数，输出其中最小的k 个。
# 例如输入1，2，3，4，5，6，7 和8 这8 个数字，则最小的4 个数字为1，2，3 和4。
import heapq


def find_k_min_numbers(array, k):
    k_array = heapq.nsmallest(k ,array)
    return k_array

def find_k_min_numbers2(array, k):
    array.sort()
    return array[:k]
