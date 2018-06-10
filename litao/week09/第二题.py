#2、实现一个函数，输入字符串，判断该字符串是否不含有重复字符

"""
字典实现
def str_duplication(src_str):
    str_dict = {}
    for i in src_str:
        str_dict[i] = str_dict.get(i,0)+1
        if str_dict[i] > 1:
            return "Duplication"
    return "No duplication"
"""

#集合实现
def str_duplication(src_str):
    return 'No duplication' if len(set(src_str)) == len(src_str) else 'Dupliccation'

str_example = 'abcdefgg'
#str_example = 'abcddefg'

print(str_duplication(str_example))