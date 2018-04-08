from random import Random

def Random_Str(String_Len = 8):
    Str1 = ''
    Chars ='AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    Length = len(Chars) - 1
    random = Random()
    for i in range(String_Len):
        Str1 += Chars[random.randint(0,Length)]
    return Str1

s = set()

while True:
    if len(s)==200:
        break
    else:
        s.add(Random_Str())
        print(s)