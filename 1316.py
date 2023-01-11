def GroupWord(word):

    include_txt = list() 

    for i in range(len(word)): 
        print(i)
        print("len: ", len(word))
     
        if(len(word) > 1):
            if word[i] not in include_txt: #i번째 단어가 리스트에 없으면
                include_txt.append(word[i]) #리스트에 추가
                if word[i] == word[i+1]:
                    word = word.replace(word[i+1], "", 1)
            else:
                return False
        else:
            print("whye" , i, word)

            if word[i-1] not in include_txt:
                return True
            else: 
                return False

n = int(input())
text_list = list()
count = 0

for i in range(n):
    text = str(input())
    if(GroupWord(text)): count += 1

print(count)