#MST, 최소 신장 트리
#백준 17472 다리만들기2
from collections import deque
from collections import defaultdict

ROW, COL = map(int, input().split())
campus = []
campusmap = [[0 for _ in range(COL)] for __ in range(ROW)]
visit = [[False for _ in range(COL)] for __ in range(ROW)]
address = 1
queue = deque()
building_xy = defaultdict(list)
for _ in range(ROW):
    temp = list(map(int, input().split()))
    campus.append(temp)

dxy = [[1,0],[-1,0],[0,-1],[0,1]] # 위, 아래, 왼쪽, 오른쪽
def check_inside(x, y):
    if 0 <= y < COL and 0 <= x < ROW:
        return True
    return False

def DFS(i, j):
    # i, j : 0이 아닌 곳을 찾은 점의 x, y 좌표
    for d in dxy:
        dx, dy = d[0], d[1]
        x, y = i + dx, j + dy
        if check_inside(x, y):
            if campus[x][y] != 0 and not visit[x][y]:
                visit[x][y] = True
                campusmap[x][y] = campusmap[i][j]
                building_xy[campusmap[i][j]].append((x, y))
                DFS(x, y)

for i in range(ROW):
    for j in range(COL):
        if campus[i][j] != 0:
            if not visit[i][j]:
                campusmap[i][j] = address
                visit[i][j] = True
                building_xy[address].append((i, j))
                DFS(i, j)
                address += 1

def mst(length, x, y, dx, dy, num):
    #dx+dy의 방향으로 움직이며 이동한 경로의 길이를 length에 저장, num:출발 건물의 번호
    x, y = x+dx, y+dy
    if check_inside(x, y):
        if campusmap[x][y] != num and campusmap[x][y] != 0:
            return length, campusmap[x][y]
        elif campusmap[x][y] != num and campusmap[x][y] == 0:
            return mst(length+1, x, y, dx, dy, num)
    else:
        return -1
graph = {}
for i in range(1, len(building_xy)+1):
    builds = building_xy[i]
    for b in builds:
        queue.append(b)
    while queue:
        x, y = queue.popleft()
        for dx, dy in dxy:
            length,new_build = mst(0, x, y, dx, dy, i)
            if (i, new_build) not in graph:
                graph[(i, new_build)] = length
            elif graph[(i, new_build)] > length:
                graph[(i, new_build)] = length
print(graph)

