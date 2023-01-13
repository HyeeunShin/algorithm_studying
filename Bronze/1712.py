a, b, c = map(int, input().strip())

if (b >= c): print(-1)
else :
    print(a // (c - b) + 1)