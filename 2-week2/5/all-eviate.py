#n = int(input(""))
directions = list(map(int, input("").split()))
n = len(directions)
new = True
now = (0, 0)
bef = (3, 3)
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
        if nex != bef and d not in visited[nex]:
            shapes += 1
            if additional:
                shapes += 1
                additional = False
            visited[nex].append(d)
        else:
            additional = False
        new = False
    else:
        visited[nex] = [d]
        visited[now].append((d+4) % 8)
        new = True
        if additional:
            shapes += 1
            additional = False
    bef = now
    now = nex

print(shapes)