from heapq import *
import sys
input = sys.stdin.readline
def solve():
    # 끝 지점에서 
    M, N = map(int, input().split())
    board = [list(map(int, input().split())) for i in range(M)]
    cache = [[0] * N for i in range(M)]
    moves = [(0,1),(1,0),(-1,0),(0,-1)]
    can_go = [(board[M-1][N-1],M-1,N-1)]
    cache[M-1][N-1]= 1
    while can_go:
        _,y,x = heappop(can_go)
        for move in moves:
            nxt_y = y + move[0]
            nxt_x = x + move[1]
            if -1 < nxt_y < M and -1 < nxt_x < N and board[y][x] < board[nxt_y][nxt_x]:
                if not cache[nxt_y][nxt_x]:
                    heappush(can_go, (board[nxt_y][nxt_x], nxt_y, nxt_x))
                cache[nxt_y][nxt_x] += cache[y][x]
    print(cache[0][0])
solve()