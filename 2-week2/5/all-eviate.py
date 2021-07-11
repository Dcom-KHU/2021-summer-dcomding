from copy import deepcopy
n = int(input(""))
directions = list(map(int, input("").split()))

new = True
now = (0, 0)
visited = {now:[-1]}
shapes = 0
additional = False

for d in directions:
    if d == 0:
        nex = (now[0], now[1]+1)
    elif d == 1:
        nex = (now[0]+1, now[1]+1)
        try:
            if 7 in visited[(now[0]), now[1]+1] or 3 in visited[(now[0]+1, now[1])]:
                additional = True
            else:
                additional = False
        except:
            additional = False
    elif d == 2:
        nex = (now[0]+1, now[1])
    elif d == 3:
        nex = (now[0]+1, now[1]-1)
        try:
            if 5 in visited[(now[0], now[1]-1)] or 1 in visited[(now[0]+1, now[1])]:
                additional = True
            else:
                additional = False
        except:
            additional = False
    elif d == 4:
        nex = (now[0], now[1]-1)
    elif d == 5:
        nex = (now[0]-1, now[1]-1)
        try:
            if 7 in visited[(now[0]-1, now[1])] or 3 in visited[(now[0], now[1]-1)]:
                additional = True
            else:
                additional = False
        except:
            additional = False
    elif d == 6:
        nex = (now[0]-1, now[1])
    elif d == 7:
        nex = (now[0]-1, now[1]+1)
        try:
            if 5 in visited[(now[0]-1, now[1])] or 1 in visited[(now[0], now[1]+1)]:
                additional = True
            else:
                additional = False
        except:
            additional = False
    if nex in visited:
        if d not in visited[nex]:
            shapes += 1
            visited[nex].append(d)
            if additional:
                shapes += 1
                additional = False
        new = False
    else:
        visited[nex] = [d]
        new = True
    now = nex

print(shapes)