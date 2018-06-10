# 1、实现数据结构stack(栈)，并实现它的append，pop方法【动手查询相关资料理解stack特点以及与queue区别】
# stack 是先进后出数据结构 进：1->2->3  出：<-1<-2<-3
# queue 是先进先出数据结构 进：1->2->3  出：<-3<-2<-1

class Node:
    def __init__(self, value):
        self.value = value
        self._next = None

    def get_next(self):
        return self._next

    def set_next(self, node):
        self._next = node


class Stack:
    def __init__(self):
        self.head = None


    def append(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def pop(self):
        if self.head is None:
            return
        tmp = self.head
        node = self.head.get_next()
        self.head = node
        return tmp.value


 # test
l1 = [1,5,3,2,5,6]
stack = Stack()
for x in l1:
    stack.append(x)

for y in l1:
    print(stack.pop())



# 2、打印出N对合理的括号组合。
# 例如： 当N=3，输出：()()(),()(()),(())(),((())),(()())


def print_parenthesis(output, opend, close, pairs):
    """
    左右括号数量匹配
    :param output:
    :param opend:
    :param close:
    :param pairs:
    :return:
    """
    if opend == pairs and close == pairs:
        print(output)
    else:
        if opend<pairs:
            print_parenthesis(output+'(', opend+1, close, pairs)
        if close<opend:
            print_parenthesis(output+')', opend, close+1, pairs)

print_parenthesis('', 0, 0, 3)

# 3、根据字典，从一个抹去空格的字符串里面提取出全部单词组合，并且拼接成正常的句子:
# 例如: 输入一个字符串："thisisanexample", 程序输出: "this is an example"


def word_break(inputs:str, word_set:set, memorized:dict):
    """
    深度优先搜索，对单词字符串进行迭代，
    查看是否在字典集合中，找到后，对剩下的字符进行递归调用
    :param inputs: 输入的字符串
    :param word_set: 单词字典
    :param memorized: 缓存字典，用来记忆化搜索，加速计算
    :return:
    """
    if inputs in memorized:
        return memorized[inputs]
    res = []
    if len(inputs) == 0:
        return res
    if inputs in word_set:
        res.append(inputs)
    for i in range(1, len(inputs)):
        word = inputs[:i]
        if word not in word_set:
            continue
        suffix = inputs[i:]
        segmentions = word_break(suffix, word_set, memorized)
        for segmention in segmentions:
            res.append(word + ' ' + segmention)

    memorized[inputs] = res
    return res

# test
ins = 'thisisanexample'
sd = {'this', 'is', 'an','example', }
d = {}
print(word_break(ins, sd, d))