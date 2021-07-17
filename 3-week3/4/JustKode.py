from collections import deque

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(n)]
checked = set()
group_key_index = 0
group_key = ['A', 'B', 'C', 'D', 'E', 'F']
group = {}
road = {}


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
                dfs(nx, ny, key)


def find_road(x, y, dx, dy, start, depth):
    nx = x + dx
    ny = y + dy

    if 0 <= nx < n and 0 <= ny < m:
        for key in group:
            if key == start:
                continue

            if arr[nx][ny] == 0:
                find_road(nx, ny, dx, dy, start, depth + 1)
            elif (nx, ny) in group[key] and depth >= 2:
                road[start][key] = min(road[start][key], depth)



for i in range(n):
    for j in range(m):
        if arr[i][j] == 1 and (i, j) not in checked:
            key = group_key[group_key_index]
            group[key] = [(i,)]
            dfs(i, j, key)
            group_key_index += 1


for key in group:
    road[key] = {}

    for key_2 in group:
        if key == key_2:
            continue
        road[key][key_2] = 1000

for key in group:
    for element in group[key]:
        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]

        for i in range(4):
            nx = element[0] + dx[i]
            ny = element[1] + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                find_road(element[0], element[1], dx[i], dy[i], key, 0)




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

if cost >= 1000:
    print(-1)
else:
    print(cost)
