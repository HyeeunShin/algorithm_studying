def GroupWord(word):

    in_text = list()

    for i in range(len(word)):
        if word[i] in in_text:
            return False
        else:
            if (i+1) < len(word):
                in_text.append(word[i])
                if(word[i] != word[i+1]):
                    in_text.append(word[i+1])
                else:
                    word = word.replace(word[i+1], "", 1)
                return True

n = int(input())
text_list = list()
count = 0

for i in range(n):
    text = str(input())
    if(GroupWord(text)): count += 1

print(count)




