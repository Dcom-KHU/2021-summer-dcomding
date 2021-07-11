n = int(input(""))
directions = list(map(int, input("").split()))

mov = [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]

new = True
now = (0, 0)
bef = (3, 3)
visited = {now:[-1]}
shapes = 0
additional = False

for d in directions:
    nex = (now[0]+mov[d][0], now[1]+mov[d][1])
    if d%2 == 1:
        if (d+2)%8 in visited[ (now[0]+mov[(d+1)%8][0]) , (now[1]+mov[(d+1)%8][1]) ]:
            additional = True
    
    if nex in visited:
        if d not in visited[nex]:
            shapes += 1
            if additional:
                shapes += 1
                additional = False
            visited[nex].append(d)
            visited[now].append((d+4) % 8)
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

    # if d == 0:
    #     nex = (now[0], now[1]+1)
    # elif d == 1:
    #     nex = (now[0]+1, now[1]+1)
    #     try:
    #         if 7 in visited[(now[0]), now[1]+1] or 3 in visited[(now[0]+1, now[1])]:
    #             additional = True
    #         else:
    #             additional = False
    #     except:
    #         additional = False
    # elif d == 2:
    #     nex = (now[0]+1, now[1])
    # elif d == 3:
    #     nex = (now[0]+1, now[1]-1)
    #     try:
    #         if 5 in visited[(now[0], now[1]-1)] or 1 in visited[(now[0]+1, now[1])]:
    #             additional = True
    #         else:
    #             additional = False
    #     except:
    #         additional = False
    # elif d == 4:
    #     nex = (now[0], now[1]-1)
    # elif d == 5:
    #     nex = (now[0]-1, now[1]-1)
    #     try:
    #         if 7 in visited[(now[0]-1, now[1])] or 3 in visited[(now[0], now[1]-1)]:
    #             additional = True
    #         else:
    #             additional = False
    #     except:
    #         additional = False
    # elif d == 6:
    #     nex = (now[0]-1, now[1])
    # elif d == 7:
    #     nex = (now[0]-1, now[1]+1)
    #     try:
    #         if 5 in visited[(now[0]-1, now[1])] or 1 in visited[(now[0], now[1]+1)]:
    #             additional = True
    #         else:
    #             additional = False
    #     except:
    #         additional = False
    # if nex in visited:
    #     if nex != bef and d not in visited[nex]:
    #         shapes += 1
    #         if additional:
    #             shapes += 1
    #             additional = False
    #         visited[nex].append(d)
    #     else:
    #         additional = False
    #     new = False
    # else:
    #     visited[nex] = [d]
    #     visited[now].append((d+4) % 8)
    #     new = True
    #     if additional:
    #         shapes += 1
    #         additional = False
    # bef = now
    # now = nex

print(shapes)