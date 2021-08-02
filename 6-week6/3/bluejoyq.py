from collections import deque
import sys
input = sys.stdin.readline
def solve():
    M, N = map(int, input().split())
    board = [list(map(int, input().split())) for i in range(M)]
    cache = [[0] * N for i in range(M)]
    moves = [(0,1),(1,0),(-1,0),(0,-1)]
    can_go = deque([(0,0)])
    cache[0][0]= 1
    while can_go:
        y,x = can_go.popleft()

        for move in moves:
            nxt_y = y + move[0]
            nxt_x = x + move[1]
            if -1 < nxt_y < M and -1 < nxt_x < N and board[y][x] > board[nxt_y][nxt_x]:
                can_go.append((nxt_y,nxt_x))
                cache[nxt_y][nxt_x] += 1
    print(cache[M-1][N-1])
solve()