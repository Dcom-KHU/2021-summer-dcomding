n = int(input())
items = [input() for i in range(n)]

groups = dict()
for i, v in enumerate(items):
    groups.setdefault(v, [])
    groups[v].append(i+1)

seq = sorted(groups.values(), key=lambda x: len(x))
result = list()
for i in seq[0]:
    start, end = i, i
    for indexes in seq[1:]:
        lst = sorted([sorted(indexes, key=lambda x: (abs(x-(start+end)/2), x))[0], start, end])
        start, end = lst[0], lst[-1]
    result.append([start, end])

for k in sorted(result, key=lambda x: (x[1]-x[0], x[0]))[0]:
    print(k)
