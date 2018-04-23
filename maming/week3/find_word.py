import re

f1=open("/x/x/x/","r+")
ceontent=f1.read()
f1.colse()

words=re.findall("[a-zA-Z]+",content)
uniq_word=set(words)

print("/x/x/x/ has {} words".format(len(uniq_word)))
