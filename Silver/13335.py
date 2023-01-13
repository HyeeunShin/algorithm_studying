n, w, L = map(int, input().split())
truck = list(map(int, input().split()))

temp = [0] * w #다리의 칸 
time = 0

while temp:
    time += 1
    temp.pop(0) 

    if truck:
        if sum(temp) + truck[0] <= L: #트럭+다리위트럭 <= L
            temp.append(truck.pop(0)) #다리위에 트럭이 또 들어와
        else:
            temp.append(0) 

print(time)
