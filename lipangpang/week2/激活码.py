print("\n".join([__import__("hashlib").md5(str(__import__("uuid").uuid1()).encode("utf-8")).hexdigest() for x in range(200)]))


print("\n".join([__import__("hashlib").md5(str(__import__("uuid").uuid1()).encode("utf-8")).hexdigest() for x in range(200)]))