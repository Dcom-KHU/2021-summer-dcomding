# 로봇의 방향에 따른 두 가지 케이스를 둬야할듯
# 세로 방향일 때, 가로 방향일 때. 기준 좌표는 (r, c)
# 회전이 가능할 때는 회전을 하는 것이 이득이다.
# 최단 경로를 찾는 미로이니 만큼 bfs를 이용하자.
# 방문한 곳은 2로 표시
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
coords = []
for _ in range(N):
    # 가로로 놓였을 때 세로로 놓였을 때
    row = list(map(lambda n: [int(n), int(n)], input().split()))
    coords.append(row)

# 각 칸에 이동하기 위한 최소 거리들을 메모
costs = [[0 for _ in range(N)] for _ in range(N)]

# direction이 0이면 가로, 1이면 세로
# r, c, direction, dist
q = deque([(0, 0, 0, 0)])
# 방문 처리
coords[0][0][0] = 2
coords[0][0][1] = 2

move_drdc = [
    [0, 1],
    [-1, 0],
    [0, -1],
    [1, 0],
]

# 다음 좌표가 방문할 수 있는 곳인가?
def is_visitable_coord(direction, nr, nc):
    # 가로
    if direction == 0:
        return 0 <= nr < N and 0 <= nc + 1 < N and (coords[nr][nc+1][direction] == 0)
    # 세로
    elif direction == 1:
        return 0 <= nr + 1< N and 0 <= nc < N and (coords[nr+1][nc][direction] == 0)

def is_rotatable_coord(direction, cr, cc, nr, nc):
    # 가로
    if direction == 0:
        delta = nc - cc
        tmp_r, tmp_c = cc, cc + delta

    else:
        delta = nr - cr
        tmp_r, tmp_c = cr + delta, cc
    # 거쳐가는 곳이 벽이 아니고
    # 회전해서 해당 방향에 놓이는 것이 방문한 적 없는 것일 때
    return 0 <= tmp_r < N and 0 <= tmp_c < N and coords[tmp_r][tmp_c][direction] != 1 and \
           0 <= nr < N and 0 <= nc < N and coords[nr][nc][(direction+1)%2] == 0

answer = int(1e10)
while q:
    cr, cc, direction, dist = q.popleft()
    # print(cr, cc, dist)
    if (direction == 0 and cr == N-1 and cc == N-2) or (direction == 1 and cr == N-2 and cc == N-1):
        answer = min(answer, dist)

    for dr, dc in move_drdc:
        nr, nc = cr + dr, cc + dc
        if is_visitable_coord(direction, nr, nc):
            q.append((nr, nc, direction, dist+1))
            coords[nr][nc][direction] = 2
        if is_rotatable_coord(direction, cr, cc, nr, nc):
            q.append((nr, nc, (direction+1) % 2, dist + 1))
            coords[nr][nc][(direction+1) % 2] = 2
print(answer)