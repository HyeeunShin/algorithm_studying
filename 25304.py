sumX = int(input())
n = int(input())

sumY = 0
for i in range(n):
    a, b = input().split()
    sumY += int(a)*int(b)

if sumX == sumY:
    print("Yes")
else: print("No")