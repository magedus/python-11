
str1="Li Keqiang Attends the 7th China-Japan-ROK Leaders' Meeting"
str2="the 7th C"

def compstr(str1,str2):
    occur=None
    lonstr=len(str1) if len(str1)>=len(str2) else len(str2)
    shostr=len(str2) if len(str2)<=len(str1) else len(str1)
    for item in range(lonstr):
        if str1[item:item+shostr] == str2:
            occur=item
            break
        else:
            continue
    return occur

print("The same index occur {}".format(compstr(str1,str2)))