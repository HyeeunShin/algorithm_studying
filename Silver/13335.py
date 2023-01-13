n, w, L = map(int, input().split())
truck = list(map(int, input().split()))

sum = 0
passBull = False
for i in range(n):
    print("i: ", i)

    if passBull: 
        passBull = False
        pass

    if (i+1) < n:
        if(truck[i] + truck[i+1] <= L):
            sum += (w*2 - 1)
            passBull = True
        else:
            sum += w
    else:
        sum += w + 1
        
    print("sum: ", sum)


print(sum)