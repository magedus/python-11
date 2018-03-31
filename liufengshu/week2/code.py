import hashlib, uuid

for n in range(200):
    h1 = hashlib.md5()
    h1.update(str(uuid.uuid1()).encode('utf-8'))
    print(h1.hexdigest())

