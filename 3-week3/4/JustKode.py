from collections import deque

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(n)]
checked = set()
group_key_index = 0
group_key = ['A', 'B', 'C', 'D', 'E', 'F']
group = {}
road = {}
loc_to_group = {}


def dfs(x, y, key):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    if (x, y) in checked:
        return
    else:
        checked.add((x, y))

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 1:
            if (nx, ny) not in group[key]:
                group[key].append((nx, ny))
                loc_to_group[(nx, ny)] = key
                dfs(nx, ny, key)


def find_road(x, y, dx, dy, current, depth):
    nx = x + dx
    ny = y + dy

    if 0 <= nx < n and 0 <= ny < m:
        if arr[nx][ny] == 0:
            if current == 'null':
                find_road(nx, ny, dx, dy, current, depth)
            else:
                find_road(nx, ny, dx, dy, current, depth + 1)
        else:
            if current == 'null':
                find_road(nx, ny, dx, dy, loc_to_group[(nx, ny)], depth)
            else:
                if loc_to_group[(nx, ny)] == current:
                    find_road(nx, ny, dx, dy, current, depth)
                elif depth >= 2:
                    road[current][loc_to_group[(nx, ny)]] = depth
                    road[loc_to_group[(nx, ny)]][current] = depth
                    find_road(nx, ny, dx, dy, loc_to_group[(nx, ny)], 0)
                else:
                    find_road(nx, ny, dx, dy, loc_to_group[(nx, ny)], 0)




for i in range(n):
    for j in range(m):
        if arr[i][j] == 1 and (i, j) not in checked:
            key = group_key[group_key_index]
            loc_to_group[(i, j)] = key
            group[key] = [(i, j)]
            dfs(i, j, key)
            group_key_index += 1


for key in group:
    road[key] = {}

    for key_2 in group:
        if key == key_2:
            continue
        road[key][key_2] = 1000

# x에 대한 길
for i in range(n):
    if (i, 0) in loc_to_group:
        find_road(i, 0, 0, 1, loc_to_group[(i, 0)], 0)
    else:
        find_road(i, 0, 0, 1, 'null', 0)

# y에 대한 길
for i in range(m):
    if (0, i) in loc_to_group:
        find_road(0, i, 1, 0, loc_to_group[(0, i)], 0)
    else:
        find_road(0, i, 1, 0, 'null', 0)

graph = []

for start in road:
    for end in road:
        if start != end and (min(start, end), max(start, end), road[start][end]) not in graph:
            graph.append((min(start, end), max(start, end), road[start][end]))

graph.sort(key=lambda x: x[2])
p = {key: key for key in road}

def find(u):
    if u != p[u]:
        p[u] = find(p[u])
    return p[u]

def union(u, v):
    r1 = find(u)
    r2 = find(v)
    p[r2] = r1

edges = 0
cost = 0

while True:
    if edges == len(group) - 1:
        break

    u, v, weight = graph.pop(0)

    if find(u) != find(v):
        union(u, v)
        cost += weight
        edges += 1
        print(cost)

if cost >= 1000:
    print(-1)
else:
    print(cost)
