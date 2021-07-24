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


# 다음 좌표가 방문할 곳인지 판단
def is_visitable_coord(direction, nr, nc):
    # 가로
    if direction == 0:
        return 0 <= nr < N and 0 <= nc < N - 1 and (coords[nr][nc][direction] == 0) and (
                    coords[nr][nc + 1][direction] != 1)
    # 세로
    elif direction == 1:
        return 0 <= nr < N - 1 and 0 <= nc < N and (coords[nr][nc][direction] == 0) and (
                    coords[nr + 1][nc][direction] != 1)


# 빡치지만 회전해서 방문할 곳인가를 판단
def is_rotatable_coord(orientation, clock, is_pivot, cc, cr):
    # 초깃값
    nr, nc, tmp_r, tmp_c = -1, -1, -1, -1
    # 가로일 때
    if orientation == 0:
        # 시계 반대 방향이면
        if not clock and is_pivot:
            nr, nc = cr - 1, cc
            tmp_r, tmp_c = cr - 1, cc + 1
        elif not clock and not is_pivot:
            nr, nc = cr, cc + 1
            tmp_r, tmp_c = cr + 1, cc
        elif clock and is_pivot:
            nr, nc = cr, cc
            tmp_r, tmp_c = cr + 1, cc + 1
        elif clock and not is_pivot:
            nr, nc = cr - 1, cc + 1
            tmp_r, tmp_c = cr - 1, cc
    # 세로일 때
    else:
        # 시계 반대 방향이면
        if not clock and is_pivot:
            nr, nc = cr, cc
            tmp_r, tmp_c = cr + 1, cc + 1
        elif not clock and not is_pivot:
            nr, nc = cr + 1, cc - 1
            tmp_r, tmp_c = cr, cc - 1
        # 시계 방향이면
        elif clock and is_pivot:
            nr, nc = cr, cc - 1
            tmp_r, tmp_c = cr + 1, cc - 1
        elif clock and not is_pivot:
            nr, nc = cr + 1, cc
            tmp_r, tmp_c = cr, cc + 1
        else:
            raise RuntimeError()

    is_next_not_wall = False
    if (direction + 1) % 2 == 0:
        is_next_not_wall = 0 <= nr < N and 0 <= nc + 1 < N and (coords[nr][nc + 1][0] != 1)
    # 세로
    elif (direction + 1) % 2 == 1:
        is_next_not_wall = 0 <= nr + 1 < N and 0 <= nc < N and (coords[nr + 1][nc][1] != 1)

    # print(f'회전 ({nc}, {nc})')
    # print('tmp_r', tmp_r)
    # print('tmp_c', tmp_c)
    # print('회전 시 거쳐가는 좌표가 벽인가?', coords[tmp_r][tmp_c][direction] != 1)
    # print('다음 나의 좌표가 방문하지 않았던 좌표인가?', coords[nr][nc][(direction+1)%2] == 0)
    # print('다음 나의 좌표가 벽인가?', is_next_not_wall)
    # print()
    return nr, nc, 0 <= tmp_r < N and 0 <= tmp_c < N and coords[tmp_r][tmp_c][direction] != 1 and \
           0 <= nr < N and 0 <= nc < N and coords[nr][nc][(direction + 1) % 2] == 0 and is_next_not_wall
# 최솟값을 정답으로하기 위해 최댓값 설정 (근데 이렇게 설정해도 되나 잘 몰겠네)
answer = int(1e10)
while q:
    cr, cc, direction, dist = q.popleft()
    # print(f'큐에서 뽑음 ({cr}, {cc}), {"가로" if direction == 0 else "세로"}, {dist}')
    if (direction == 0 and cr == N-1 and cc == N-2) or (direction == 1 and cr == N-2 and cc == N-1):
        answer = min(answer, dist)

    for dr, dc in move_drdc:
        nr, nc = cr + dr, cc + dc
        if is_visitable_coord(direction, nr, nc):
            q.append((nr, nc, direction, dist+1))
            coords[nr][nc][direction] = 2
    for clock, is_pivot in [(False,False), (False,True), (True,False), (True,True)]:
        nr, nc, is_rotatable = is_rotatable_coord(direction, clock, is_pivot, cc, cr)
        if is_rotatable:
            q.append((nr, nc, (direction + 1) % 2, dist + 1))
            coords[nr][nc][(direction+1) % 2] = 2
        #
        # if is_rotatable_coord(direction, cr, cc, nr, nc):
        #     if nr < 0:
        #         print("ERROR ROT")
        #     q.append((nr, nc, (direction+1) % 2, dist + 1))
        #     coords[nr][nc][(direction+1) % 2] = 2

print(answer)