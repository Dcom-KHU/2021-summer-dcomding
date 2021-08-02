from collections import defaultdict

a, b = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

dc = defaultdict(int)
for n in A+B:
    dc[n] += 1

count = 0
for v in dc.values():
    if v == 1:
        count += 1

print(count)
