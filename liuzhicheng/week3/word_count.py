contents ="State police spokesman Sgt. John Perrine says investigators don’t know exactly how much cash was in the truck when its lost its load about 9 a.m. Wednesday on Interstate 70 on the city’s southwest side. Perrine says it was definitely hundreds of thousands.\nOfficers blocked traffic as they helped collect money from along the highway. Perrine says an undetermined amount remains unaccounted for as some drivers stopped to scoop up cash.\nPerrine says anyone who picked up the money could be charged with theft and he urged them to contact state police to return it."
words = contents.replace(',',' ').replace('.',' ').replace('\n',' ').split()
count = {x:0 for x in set(words)}

for word in count.keys():
    count[word] = words.count(word)

print(sorted(count.items(),key=lambda x:x[0]))