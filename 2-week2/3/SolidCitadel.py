from collections import deque

n = int(input())
tickets = [input().split() for i in range(n)]

groups = dict()
for t in tickets:
    if t[0] in groups.keys():
        groups[t[0]].append(t[1])
    else:
        groups[t[0]] = [t[1]]

groups = {k: sorted(sorted(v), key=lambda x: len(x)) for k, v in groups.items()}

queue = deque([(['DCOM'], groups)])
while len(queue):
    route, groups = queue.popleft()
    f = route[-1]
    if f in groups.keys():
        for t in groups[f]:
            newgroup = {k: v[:] for k, v in groups.items() if len(v)}
            newgroup[f].remove(t)
            queue.append([route+[t], newgroup])
    elif len(route) == n+1 and len(groups) == 1:
        break
print(' '.join(route))
