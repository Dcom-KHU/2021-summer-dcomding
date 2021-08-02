n = int(input())
eraser = [i for i in range(n+1)]
while len(eraser) > 2:
    temp = [0]
    for i in range(1,len(eraser)):
        if i%2 == 0:
            temp.append(eraser[i])
    eraser = temp
print(eraser[1])