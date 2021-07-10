from collections import deque

n = int(input())
tickets = [input().split() for i in range(n)]

groups = {'start':['DCOM']}
for t in tickets:
    groups.setdefault(t[0], [])
    groups[t[0]].append(t[1])

groups = {k: sorted(sorted(v), key=lambda x: len(x)) for k, v in groups.items()}
route = [('start', 0)]

queue = deque([route])
while len(queue):
    route = queue.popleft()
    f = groups[route[-1][0]][route[-1][1]]
    if f in groups.keys():
        for i in range(len(groups[f])):
            if (f, i) not in route:
                queue.append((route+[(f, i)]))
    if len(route) == n+1:
        break
    
print(' '.join([groups[f][i] for f, i in route]))
