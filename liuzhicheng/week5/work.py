# Q1
import random
alist = [1,2,3,4,5]
print(alist)
random.shuffle(alist)
print(alist)

# Q2
import random
inventory = {'袜子':10, '鞋子':20, '拖鞋':30, '项链':40}

def show(inventory):
    products = list(inventory.keys())
    product_section=[]

    for i in range(len(products)):
        if i ==0:
            product_section.append(inventory[products[i]])
        else:
            product_section.append(inventory[products[i]] + product_section[-1])

    x = random.randint(1,product_section[-1])

    for i in range(len(products)):
        if x <= product_section[i]:
            print(products[i])
            break

show(inventory)