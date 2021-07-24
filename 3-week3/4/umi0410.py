from collections import deque
from functools import reduce
from copy import deepcopy
HEIGHT, WIDTH = map(int, input().split())
coord = []
for _ in range(HEIGHT):
    coord.append(list(map(int, input().split())))

d = [
    [0,1],
    [1,0],
    [0,-1],
    [-1,0],
]

bridge_q = deque([])
def is_movable(current_coord, dydx):
    if current_coord[0] + dydx[0] < 0 or current_coord[0] + dydx[0] >= HEIGHT:
        return False
    if current_coord[1] + dydx[1] < 0 or current_coord[1] + dydx[1] >= WIDTH:
        return False
    return True

# bfs로 현재 섬에서 갈 수 있는 섬들을 찾는다.
def bfs_island_number(coord, q:deque, number):
    while len(q) != 0:
        rc = q.pop()
        for dydx in d:
            if is_movable(rc, dydx):
                next_r = rc[0] + dydx[0]
                next_c = rc[1] + dydx[1]
                if coord[next_r][next_c] == 1:
                    coord[next_r][next_c] = number
                    q.append([next_r, next_c])
                    bridge_q.append([next_r, next_c])

def make_bridges(bq:deque):
    while(len(bq) != 0):
        cr, cc = bq.pop()
        island = coord[cr][cc]
        if cr == HEIGHT-1 or cr == 0 or coord[cr + 1][cc] != island or coord[cr - 1][cc] != island:
            for tr in range(HEIGHT):
                if coord[tr][cc] > 1 and coord[tr][cc] != island  and abs(tr - cr) - 1 >= 2:
                    bridges[island][coord[tr][cc]] = min(bridges[island][coord[tr][cc]], abs(tr - cr) - 1)
        if cc == WIDTH - 1 or cc == 0 or coord[cr][cc+1] != island or coord[cr][cc-1] != island:
            for tc in range(WIDTH):
                if coord[cr][tc] > 1 and coord[cr][tc] != island  and abs(tc - cc) - 1 >= 2:
                    bridges[island][coord[cr][tc]] = min(bridges[island][coord[cr][tc]], abs(tc - cc) - 1)

def only_shortest_brides(bridges):
    connections = [[0 for _ in range(number + 1)] for _ in range(number + 1)] # 2,3,4 섬으로 3개일 때 5칸을 만들어 앞에 두칸은 버리고 [2], [3], [4] 이용
    data = []
    for start_island in range(len(bridges)):
        for dest_island in range(start_island + 1, len(bridges)):
            # 거리, 시작섬, 도착섬 순으로 정렬할 수 있게함.
            # 101은 유효하지 않은 값
            if bridges[start_island][dest_island] != 101 and bridges[start_island][dest_island] > 1:
                data.append([bridges[start_island][dest_island], start_island, dest_island])
    data.sort()
    distance_sum = 0
    for distance, start_island, dest_island in data:
        if bridges[start_island][dest_island] != 101:
            connections[start_island][dest_island] = 1
            connections[dest_island][start_island] = 1
            distance_sum += distance
            if check_all_connected(deepcopy(connections)):
                return distance_sum
    return -1

def check_all_connected(connections):
    num_of_island = len(connections)
    visit_info = [False] * num_of_island
    q = deque([])
    for start_island in range(2, num_of_island):
        for dest_island in range(2, num_of_island):
            if connections[start_island][dest_island] != 0:
                visit_info[start_island] = True
                visit_info[dest_island] = True
                q.append(dest_island)
                # 방문 처리
                connections[start_island][dest_island] = 0
                connections[dest_island][start_island] = 0
        if len(q) != 0:
            # 첫 번째 방문섬을 찾은 거니 break
            break
    while(len(q) != 0):
        current_island = q.pop()

        for dest_island in range(2, num_of_island):
            if connections[current_island][dest_island] != 0:
                q.append(dest_island)
                # 방문 처리
                connections[current_island][dest_island] = 0
                connections[dest_island][current_island] = 0
                visit_info[dest_island] = True

    return reduce(lambda r, v: r and v, visit_info[2:])




number = 1
for r in range(HEIGHT):
    for c in range(WIDTH):
        if coord[r][c] == 1:
            number += 1
            coord[r][c] = number
            bridge_q.append([r,c])
            bfs_island_number(coord, deque([[r,c]]), number)
# 섬의 개수는 number -1개
# 어떤 섬에서 어떤 섬까지 가는 거리
# 섬이 3개(cnt = 4) 0번, 1번은 dummy 2,3,4번 섬 존재
bridges = [ [101 for _ in range(number + 1)] for _ in range(number + 1)]

for row in coord:
    print(row)
make_bridges(bridge_q)
print(only_shortest_brides(bridges))

# print(bridges)





