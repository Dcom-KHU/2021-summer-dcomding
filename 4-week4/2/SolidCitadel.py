n = int(input())
times = sorted([tuple(map(int, input().split())) for i in range(n)], key= lambda x: (x[1], x[0]))

cur, count = 0, 0
for t in times:
    if cur <= t[0]:
        cur = t[1]
        count += 1

print(count)
