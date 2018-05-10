li = [ [ ] ] * 5
li[0].append(10)
print(li)
li[1].append(20)
print(li)
li.append(30)
print(li)

#[[]]*5列表中有5个空列表元素，且这5个列表元素是同一个列表对象，即同一个引用，故对li[0],li[1]操作时，对那5个列表元素的影响是一致的
#li.append(30)此操作是对li列表新追加一个元素