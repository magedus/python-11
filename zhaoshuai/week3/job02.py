textPath='MyFather.txt'
with open(textPath,'r',encoding='utf-8') as f:
    wordList=f.read().split()
print(wordList)

for x in range(len(wordList)):
    wordList[x]=wordList[x].strip(',.!@#$%^&*()"?><:"{}[];=+').lower()
print(wordList)

wordDict={}
for x in range(len(wordList)):
    if  wordDict.get(wordList[x]):
        pass
    else:
        wordDict[wordList[x]]=wordList.count(wordList[x])
count=zip(wordDict.values(),wordDict.keys())
print(sorted(count,reverse=True))
