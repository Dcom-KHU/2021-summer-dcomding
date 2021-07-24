n = int(input())
times = sorted([tuple(map(int, input().split())) for i in range(n)], key=lambda x: (x[1],x[0]))

cur, sum = 0
for time in times:
    if (cur <= time[0]):
        sum += 1
        cur = time[1]
        
    else:
        pass
