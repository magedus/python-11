num = 121121
num_str = str(num)
num_length = len(num_str)
palindrome = False
if num_length == 1:
    palindrome = True
else:
    for i in range(num_length//2):
        if num_str[i] != num_str[-1-i]:
            break
    else:
        palindrome = True
if palindrome:
    print("Number {} is a palindromic number.".format(num))
else:
    print("Number {} is not a palindromic number.".format(num))
