# 1、实现数据结构stack(栈)，并实现它的append，pop方法【动手查询相关资料理解stack特点以及与queue区别】
# 2、打印出N对合理的括号组合。
# 例如： 当N=3，输出：()()(),()(()),(())(),((()))
# 3、根据字典，从一个抹去空格的字符串里面提取出全部单词组合，并且拼接成正常的句子:
# 例如: 输入一个字符串："thisisanexample", 程序输出: "this is an example"
# 温馨提示：请于6月3号，本周完成


# 第一题
# class Stack(object):
#     def __init__(self):
#         self.stack=[]
#     def isEmpty(self):
#         return self.stack==[]
#     def push(self,item):
#         self.stack.append(item)
#     def pop(self):
#         if self.isEmpty():
#             raise IndexError,'pop from empty stack'
#         return self.stack.pop()



#第二题
# def foo(output='',open=0,close=0,num=3):
#     if open==num and close==num:
#         print(output)
#     else:
#         if open < num:
#             foo(output+'(',open+1,close,num)
#         if close < open:
#             foo(output+')',open,close+1,num)
# foo()



#第三题
# s = '''thisisanexample'''
# import re
#
# target = []
# def match_word(word:str,target=None):
#     if target is None:
#         target = []
#
#     lst = ['an', 'this', 'at', 'is', 'you', 'are', 'example', 'not']
#     while word:
#         for x in lst:
#             matcher = re.match(x,word)
#             if matcher:
#                 target.append(matcher.group())
#                 word = word[len(matcher.group()):]
#     return ' '.join(target)
# print(match_word(s))
