lit=[1,2,3,2,1]
lit2=[1,2,3,4,5]

def is_PalindromeA(lit):
      tempList=list(reversed(lit))
      print("回文") if tempList==lit else print("不是回文")

def is_PalindromeB(lit):
      tempList=lit[::-1]
      print("回文") if tempList==lit else print("不是回文")

is_PalindromeA(lit)
is_PalindromeA(lit2)

is_PalindromeB(lit)
is_PalindromeB(lit2)

