def GroupWord(word):

    txtList = list() 

    for i in range(len(word)): 
        if word[i] not in txtList:
            txtList.append(word[i])
        elif (word[i] in txtList) & (word[i] == word[i-1]):
            word = word.replace(word[i], " ", 1)
        elif (word[i] in txtList) & (word[i] != word[i-1]):
            return False
    
    return True



n = int(input())
text_list = list()
count = 0

for i in range(n):
    text = str(input())
    if(GroupWord(text)): count += 1

print(count)