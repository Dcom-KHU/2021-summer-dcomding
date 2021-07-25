from collections import deque

class Pos(tuple):
    def __add__(self, other):
        return Pos((self[0] + other[0], self[1] + other[1]))

    def __sub__(self, other):
        return Pos((self[0] - other[0], self[1] - other[1]))

n = int(input())
#board[x, y] : 0은 빈칸, 1은 벽
board = {(x+1, y+1): int(p) for y in range(n) for x, p in enumerate(input().split())}
for x in range(n+2):
    for y in [0, n+1]:
        board[x, y] = 1
        board[y, x] = 1

dp = dict()
#p는 (x, y)좌표, d는 (0, 1), (1, 0), (0, -1), (-1, 0)중 하나로 로봇이 차지하는 두 칸을 p와 p+d로 표현
#dp[p, d] : p, p+d칸에 도착하는 최단시간. 초기값 inf, 불가능할 경우 0
for y in range(n+2):
    for x in range(n+2):
        p = Pos((x, y))
        if board[p] == 0:
            for d in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                dp[p, d] = 0 if board[p+d] else float('inf')

#BFS
queue = deque([ (0, Pos((1, 1)), (1, 0)) ])
while queue:
    time, pos1, direction = queue.popleft()
    time += 1
    pos2 = pos1 + direction
    if pos2 == (n, n):
        print(time-1)
        break
    else:
        opposite = (-direction[0], -direction[1])
        for side in (direction[1], direction[0]), (-direction[1], -direction[0]):
            if board[pos2+side] + board[pos1+side] == 0:
                for npos, ndir in (pos2, side), (pos1, side), (pos1+side, direction):
                    if time < dp[npos, ndir]:
                        queue.append((time, npos, ndir))
                        dp[npos, ndir] = time
        for npos, ndir in (pos2, direction), (pos1, opposite):
            if time < dp[npos, ndir] :
                queue.append((time, npos, ndir))
                dp[npos, ndir] = time
