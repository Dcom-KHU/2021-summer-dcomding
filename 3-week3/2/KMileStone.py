n = int(input())
table = []
for i in range(n):
    table.append(list(map(int, input().split())))


# DP : d[i+table[i][0]-1] = max(d[i-1]+table[i][1], d[i+table[i][0]-1])
d = [0 for i in range(n)]

for i in range(n):
    if d[i] < d[i-1]:
        d[i] = d[i-1]

    due_date = i+table[i][0]-1

    if due_date < n:
        d[due_date] = max(d[i-1]+table[i][1], d[due_date])

print(d[n-1])
