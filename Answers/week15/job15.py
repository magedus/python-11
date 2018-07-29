# 1、请实现一个方法将链表反转
# 举例：
# 链表a，有节点1->2->3->4  反转后为：4->3->2->1

# 步骤：首先实现一个单链表，然后实现其反转方法


class Node:

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList:

    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        # insert a new node to begin
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def print_all(self):
        current = self.head
        while current:
            print(current.get_data())
            current = current.get_next()
        print('------end-------')

    def reversed_iter(self):
        # 反转节点
        last = None
        current = self.head
        while current:
            next_node = current.get_next()
            current.set_next(last)
            last = current
            current = next_node
        self.head = last


# test

s = LinkedList()
for i in range(5):
    s.insert(i)
s.print_all()
s.reversed_iter()
s.print_all()


# 2、实现pow函数，分析其时间复杂度

def my_pow(a, n):
    if a == 0 or a == 1 or n == 1:
        return a

    if a == -1:
        if n % 2 == 0:
            return 1
        else:
            return -1

    if n == 0:
        return 1

    if n < 0:
        return 1 / my_pow(a, -n)

    val = my_pow(a, n // 2)

    if n % 2 == 0:
        return val * val
    return val * val * a


# test
print(my_pow(3, 3))
