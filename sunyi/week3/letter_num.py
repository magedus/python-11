# 判断英文文本中的单词数
# 打开文件，read方法读取文本置于string中
string = open('myheartwillgoon.txt').read()
# 以空格为切割置于base列表中
base = string.split()
# 判断base列表中的元素是否为均为单词，是的话就赋值给final，fanal的元素个数即为单词数
final = [x for x in base if x.isalpha() is True]
print(len(final))

# 原本写了一堆的循环和判断，30多行代码，后来发现利用解析式生成器和现成的方法只需要四行代码
# 感觉很激动，终于尝到了传说中的语法糖
