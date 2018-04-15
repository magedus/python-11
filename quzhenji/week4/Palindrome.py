while True:
    palindrome_num = input('please input a number>>>').strip()
    length = len(palindrome_num)

    if palindrome_num.isdigit():
        if length == 5:
            break

        else:
            print('the length of the num is not 5 bits, please input again')

for i in range(length//2):
    FLG = True
    if palindrome_num[i] != palindrome_num[-1-i]:
        FLG = False
        break

if FLG:
    print('{} is palindrome num'.format(palindrome_num))
else:
    print('{} is NOT palindrome num'.format(palindrome_num))