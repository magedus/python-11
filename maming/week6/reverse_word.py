word="Wang Yi Meets with Director-General of the International Institute for Strategic Studies in London John Chipman of the UK "

def reverse_word(src):
    print("\033[1;35m  Before reverse:\033[0m  {} ".format(src))
    result=" ".join(src.split()[::-1])[::-1]    
    print("\033[1;32m  After reverse: \033[0m {}".format(result))

reverse_word(word)
