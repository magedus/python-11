import random
import string


alpha={"".join(random.sample(string.ascii_letters+string.digits,8))for _ in range(200)}

if len(alpha)==200:
    pass
else:
    for i in range(200-len(alpha)):
        alpha.add("".join(random.sample(string.ascii_letters+string.digits,8)))

print(alpha)
