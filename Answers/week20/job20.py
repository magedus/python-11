# 1、实现3个线程交替打印 abcabcabc...，一个打印a，一个打印b，一个打印c

import time
import threading

STATE = 1

def print_a(cond: threading.Condition, e: threading.Event):
    global STATE
    while not e.is_set():
        with cond:
            if STATE == 1:
                print('a')
                STATE = 2
            cond.notify_all()
            time.sleep(1)
            cond.wait()


def print_b(cond: threading.Condition, e:threading.Event):
    global STATE
    while not e.is_set():
        with cond:
            if STATE == 2:
                print('b')
                STATE = 3
            cond.notify_all()
            time.sleep(1)
            cond.wait()

def print_c(cond: threading.Condition, e:threading.Event):
    global STATE
    while not e.is_set():
        with cond:
            if STATE == 3:
                print('c')
                STATE = 1
            cond.notify_all()
            time.sleep(1)
            cond.wait()

c1 = threading.Condition()
ev = threading.Event()
t1 = threading.Thread(target=print_a, args=(c1, ev))
t2 = threading.Thread(target=print_b, args=(c1, ev))
t3 = threading.Thread(target=print_c, args=(c1, ev))
# t1.start()
# t2.start()
# t3.start()


# 2、输入一个字符串，求不含有重复字母的最长子串长度
# 举例：输入字符串 'aaaa'，其不含有重复字母的最长子串为‘a’，输出长度为1



def length_of_longest_substring(s):
    unique_chars = set()
    j = 0
    n = len(s)
    longest = 0
    for i in range(n):
        while j < n and s[j] not in unique_chars:
            unique_chars.add(s[j])
            j += 1
        longest = max(longest, j - i)
        unique_chars.remove(s[i])

    return longest

print(length_of_longest_substring('aaa'))