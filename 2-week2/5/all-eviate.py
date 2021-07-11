from copy import deepcopy
n = int(input(""))
directions = list(map(int, input("").split()))

new = True
now = (0, 0)
visited = {now:[-1]}
shapes = 0

for d in directions:
    if d == 0:
        nex = (now[0], now[1]+1)
    elif d == 1:
        nex = (now[0]+1, now[1]+1)
    elif d == 2:
        nex = (now[0]+1, now[1])
    elif d == 3:
        nex = (now[0]+1, now[1]-1)
    elif d == 4:
        nex = (now[0], now[1]-1)
    elif d == 5:
        nex = (now[0]-1, now[1]-1)
    elif d == 6:
        nex = (now[0]-1, now[1])
    elif d == 7:
        nex = (now[0]-1, now[1]+1)
    if nex in visited:
        if d not in visited[nex]:
            shapes += 1
            visited[nex].append(d)
        new = False
    else:
        visited[nex] = [d]
        new = True
    now = nex

print(shapes)