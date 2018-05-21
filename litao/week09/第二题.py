#2、实现一个函数，输入字符串，判断该字符串是否不含有重复字符


def str_duplication(src_str):
    str_dict = {}
    for i in src_str:
        str_dict[i] = str_dict.get(i,0)+1
        if str_dict[i] > 1:
            print(i,"is a duplication strings.")
            return i
    print("This is not duplication strings.")


str_example = 'abcdefg'
#str_example = 'abcddefg'

str_duplication(str_example)