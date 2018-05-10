# 获取输入
get_str = input("please input a number:")
# 将输入保存为列表
get_list = list(get_str)
storage_list = get_list
# 将列表反转并转储，最后再转换为字符串
get_list.reverse()
reverse_list = get_list
reverse_str = "".join(get_list)
# 检查相关转换是否有误
print("input num:", get_str)
print("reverse num:",  reverse_str)
#判断是否为回文数
if get_str == reverse_str:
    print("%s is a palindrome number" % get_str)
else:
    print("%s is not a palindrome number" % get_str)
