dialList = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]

letter = list(input())
sum = 0

for p in range(len(letter)):
    for q in dialList:
        if letter[p] in q:
            sum += dialList.index(q) + 3

print(sum)