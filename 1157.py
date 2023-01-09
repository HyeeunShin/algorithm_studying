from collections import Counter

question = input().upper()

count = Counter(question)
# print(count.most_common())

if len(count) == 1:
    print(count.most_common(1)[0][0])
else:
    if count.most_common()[0][1] == count.most_common()[1][1]:
        print("?")
    else:   
        print(count.most_common(1)[0][0])

