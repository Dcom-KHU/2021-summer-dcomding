n = int(input())
boxes = list(map(int, input().split()))


# DP : d[i] = max(d which can be put in) + 1
d = [0 for i in range(n)]
max_d = 0

d[0] = 1
for i in range(n):
    # get max
    for j in range(i):
        if boxes[j] < boxes[i] and d[j] > max_d:
            max_d = d[j]

    d[i] = max_d + 1
    max_d = 0

print(d[n-1])
