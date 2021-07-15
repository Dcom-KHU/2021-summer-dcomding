N, M = map(int, input().split())
map_info = []
for i in range(N):
    map_info.append(list(map(int, input().split())))


start = (-1, -1)
count = 0
bridge_hor = []
bridge_ver = []
bridge = False

# find horizontal bridge
for i in range(N):
    count = 0
    bridge = False

    for j in range(M):
        if not bridge:
            if map_info[i][j] == 1:
                bridge = True
                start = (i, j)
        else:
            if map_info[i][j] == 0:
                count += 1
            elif map_info[i][j] == 1:
                if count > 1:
                    bridge_hor.append([count, start])
                start = (i, j)
                count = 0

# find vertical bridge
for j in range(M):
    count = 0
    bridge = False

    for i in range(N):
        if not bridge:
            if map_info[i][j] == 1:
                bridge = True
                start = (i, j)
        else:
            if map_info[i][j] == 0:
                count += 1
            elif map_info[i][j] == 1:
                if count > 1:
                    bridge_ver.append([count, start])
                start = (i, j)
                count = 0


visit_building = {}

# find building
for i in range(N):
    for j in range(M):
        if map_info[i][j] == 1:
            visit_building[(i, j)] = 0


min_length = 0
visit_bridge = {}

# add all bridges
for b in bridge_hor:
    min_length += b[0]
    i = b[1][0]
    j = b[1][1]

    for iter in range(b[0]):
        if map_info[i][j+1+iter] == 0:
            map_info[i][j+1+iter] = 'h'
        elif map_info[i][j+1+iter] == 'v':
            map_info[i][j+1+iter] = 'hv'
        visit_bridge[(i, j+1+iter)] = 0

for b in bridge_ver:
    min_length += b[0]
    i = b[1][0]
    j = b[1][1]

    for iter in range(b[0]):
        if map_info[i+1+iter][j] == 0:
            map_info[i+1+iter][j] = 'v'
        elif map_info[i+1+iter][j] == 'h':
            map_info[i+1+iter][j] = 'hv'
        visit_bridge[(i+1+iter, j)] = 0


# check connection
def visit(coord, type, dir):
    i = coord[0]
    j = coord[1]

    if type == 'v':
        try:
            visit_bridge[coord] += 1
        except:
            pass

        # directional visit
        if dir == 'u':
            # vertical bridge up
            if i - 1 >= 0 and visit_bridge.get((i - 1, j)) != None and visit_bridge.get((i - 1, j)) < len(map_info[i - 1][j]) and 'v' in map_info[i - 1][j]:
                visit((i - 1, j), 'v', 'u')
            # vertical building up
            if i - 1 >= 0 and visit_building.get((i - 1, j)) == 0:
                visit((i - 1, j), 'b', 'u')
        elif dir == 'd':
            # vertical bridge down
            if i + 1 < N and visit_bridge.get((i + 1, j)) != None and visit_bridge.get((i + 1, j)) < len(map_info[i + 1][j]) and 'v' in map_info[i + 1][j]:
                visit((i + 1, j), 'v', 'd')
            # vertical building down
            if i + 1 < N and visit_building.get((i + 1, j)) == 0:
                visit((i + 1, j), 'b', 'd')

    elif type == 'h':
        try:
            visit_bridge[coord] += 1
        except:
            pass

        # directional visit
        if dir == 'l':
            # vertical bridge left
            if j - 1 >= 0 and visit_bridge.get((i, j - 1)) != None and visit_bridge.get((i, j - 1)) < len(map_info[i][j - 1]) and 'h' in map_info[i][j - 1]:
                visit((i, j - 1), 'h', 'l')
            # vertical building left
            if j - 1 >= 0 and visit_building.get((i, j - 1)) == 0:
                visit((i, j - 1), 'b', 'l')
        elif dir == 'r':
            # horizontal bridge right
            if j + 1 < M and visit_bridge.get((i, j + 1)) != None and visit_bridge.get((i, j + 1)) < len(map_info[i][j + 1]) and 'h' in map_info[i][j + 1]:
                visit((i, j + 1), 'h', 'r')
            # horizontal building right
            if j + 1 < M and visit_building.get((i, j + 1)) == 0:
                visit((i, j + 1), 'b', 'r')

    else:
        try:
            visit_building[coord] += 1
        except:
            pass

        # visit building
        # up
        if i - 1 >= 0 and visit_building.get((i - 1, j)) == 0:
            visit((i - 1, j), 'b', 'u')
        # down
        if i + 1 < N and visit_building.get((i + 1, j)) == 0:
            visit((i + 1, j), 'b', 'd')
        # left
        if j - 1 >= 0 and visit_building.get((i, j - 1)) == 0:
            visit((i, j - 1), 'b', 'l')
        # right
        if j + 1 < M and visit_building.get((i, j + 1)) == 0:
            visit((i, j + 1), 'b', 'r')

        # visit bridge
        # up
        if i - 1 >= 0 and visit_bridge.get((i - 1, j)) != None and visit_bridge.get((i - 1, j)) < len(map_info[i - 1][j]) and 'v' in map_info[i - 1][j]:
            visit((i - 1, j), 'v', 'u')
        # down
        if i + 1 < N and visit_bridge.get((i + 1, j)) != None and visit_bridge.get((i + 1, j)) < len(map_info[i + 1][j]) and 'v' in map_info[i + 1][j]:
            visit((i + 1, j), 'v', 'd')
        # left
        if j - 1 >= 0 and visit_bridge.get((i, j - 1)) != None and visit_bridge.get((i, j - 1)) < len(map_info[i][j - 1]) and 'h' in map_info[i][j - 1]:
            visit((i, j - 1), 'h', 'l')
        # right
        if j + 1 < M and visit_bridge.get((i, j + 1)) != None and visit_bridge.get((i, j + 1)) < len(map_info[i][j + 1]) and 'h' in map_info[i][j + 1]:
            visit((i, j + 1), 'h', 'r')


# remove bridge
def remove(n):
    global valid
    global min_length
    length = 0
    bridge_included.remove(n)
    for i in bridge_included:
        if i < len(bridge_hor):
            length += bridge_hor[i][0]
        else:
            length += bridge_ver[i-len(bridge_hor)][0]

    # remove bridge
    if n < len(bridge_hor):
        b = bridge_hor[n]
        i = b[1][0]
        j = b[1][1]

        for iter in range(b[0]):
            if map_info[i][j+1+iter] == 'hv':
                map_info[i][j+1+iter] = 'v'
            elif map_info[i][j+1+iter] == 'h':
                map_info[i][j+1+iter] = 0
            if map_info[i][j+1+iter] == 0:
                del visit_bridge[(i, j+1+iter)]
    else:
        b = bridge_ver[n-len(bridge_hor)]
        i = b[1][0]
        j = b[1][1]

        for iter in range(b[0]):
            if map_info[i+1+iter][j] == 'hv':
                map_info[i+1+iter][j] = 'h'
            elif map_info[i+1+iter][j] == 'v':
                map_info[i+1+iter][j] = 0
            if map_info[i+1+iter][j] == 0:
                del visit_bridge[(i+1+iter, j)]

    # check connection
    visit(start, 'b', 'd')

    # if connected
    if 0 not in visit_building.values():
        valid = True

        # update min
        if length < min_length:
            min_length = length

        # init visit
        for key in visit_building.keys():
            visit_building[key] = 0
        for key in visit_bridge.keys():
            visit_bridge[key] = 0

        # remove more
        for i in bridge_included:
            remove(i)

    # if not connected
    else:
        # init visit
        for key in visit_building.keys():
            visit_building[key] = 0
        for key in visit_bridge.keys():
            visit_bridge[key] = 0

    # restore bridge
    if n < len(bridge_hor):
        b = bridge_hor[n]
        i = b[1][0]
        j = b[1][1]

        for iter in range(b[0]):
            if map_info[i][j+1+iter] == 0:
                map_info[i][j+1+iter] = 'h'
            elif map_info[i][j+1+iter] == 'v':
                map_info[i][j+1+iter] = 'hv'
            visit_bridge[(i, j+1+iter)] = 0
    else:
        b = bridge_ver[n - len(bridge_hor)]
        i = b[1][0]
        j = b[1][1]

        for iter in range(b[0]):
            if map_info[i+1+iter][j] == 0:
                map_info[i+1+iter][j] = 'v'
            elif map_info[i+1+iter][j] == 'h':
                map_info[i+1+iter][j] = 'hv'
            visit_bridge[(i + 1 + iter, j)] = 0

    bridge_included.append(n)
    bridge_included.sort()


valid = False
start = list(visit_building.keys())[0]
bridge_included = [i for i in range(len(bridge_hor) + len(bridge_ver))]

for i in bridge_included:
    remove(i)

if min_length == 0 or not valid:
    print(-1)
else:
    print(min_length)
