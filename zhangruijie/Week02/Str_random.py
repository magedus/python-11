
""" ASCII 
0-9 : 48~57		A-Z	: 65~90		a-z	: 97-122   (10+26+26=62)
"""


sn=[]						
sn_len = 6
sn_No = 200
pool = '1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
index = []

# generate 200 different random numbers
for i in range(200):
	raw = random.randint(0,pow(62,sn_len))
	if raw not in index:
		index.append(raw)

# random number  -> SN
for i in range(200):
	raw = index[i]
	str=[]
	for j in range(6):
		str.append(pool[raw % 62])
		raw = raw // 62
	sn.append(str)
	
# display SNs	
for i in range(200):
    print(sn[i])
	