numList = [i for i in range(1,31)]

# print(numList)
for j in range(28):
    target = int(input())
    numList.remove(target)

print(numList[0])
print(numList[1])