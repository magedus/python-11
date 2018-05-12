s1 = 'abcdefg'
s2 = 'defabcdoabcdeftw'
s3 = 'hixyz'

#method1
# def find_max_substr(str1,str2):
#     length = len(str1)
#     for substrlen in range(length,0,-1):
#         for start in range(0,length - substrlen + 1):
#             sub_str = str1[start:start + substrlen]
#             if str2.find(sub_str) > -1:
#                 print('The max substr is: {}'.format(sub_str))
#                 return sub_str
#
#     else:
#         return None
#
# print(find_max_substr(s1,s2))

#method2

#                     str1        j
#             _____________________________
#             0   1   2   3   4   5   6
#             x   x   x   x   x   x   x
#     | 0 x
#     | 1 x
# str2| 2 x
#     | 3 x
#   i | 4 x
#     | 5 x

def findmaxsubstr2(str1,str2):
    max_substr = []
    xmax = 0
    xindex = 0

    for i,x in enumerate(str2):
        max_substr.append([])
        for j,y in enumerate(str1):
            if x != y:
                max_substr[i].append(0)
            else:
                if i == 0 or j == 0 :
                    max_substr[i].append(1)
                else:
                    max_substr[i].append(max_substr[i-1][j-1] + 1)

            if max_substr[i][j] > xmax:
                xmax = max_substr[i][j]
                xindex = j
                xindex += 1
    if xmax == 0:
        return None
    else:
        return str1[xindex - xmax : xindex]

print(findmaxsubstr2(s1,s2))
