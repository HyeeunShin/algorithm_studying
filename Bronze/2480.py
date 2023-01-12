input_list = sorted(list(input().replace(" ", "")))
for i in input_list:
    i = int(i)
input_set = set(input_list)

if len(input_set) == 1:
    print(10000 + int(input_list[1]) * 1000)
elif len(input_set) == 2:
    frequentNum = max(input_list, key=input_list.count)
    print(1000 + int(frequentNum) * 100)
else:
    maxNum = max(input_list)
    print(int(maxNum) * 100)

