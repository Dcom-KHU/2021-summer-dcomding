import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

from collections import deque
drdc = [
    [0, 1],
    [-1, 0],
    [0, -1],
    [1, 0],
]

R, C = map(int, input().split())
coords = []
for _ in range(R):
    coords.append(list(map(int, input().split())))

def bfs(_coords):
    q = deque([[0, 0]])
    answer = 0
    while q:
        cr, cc = q.popleft()
        # 도착지인 경우
        if cr == R - 1 and cc == C - 1:
            answer += 1
        else:
            for dr, dc in drdc:
                nr, nc = cr + dr, cc + dc
                if 0 <= nr < R and 0 <= nc < C:
                    if _coords[nr][nc] < _coords[cr][cc]:
                        q.append([nr, nc])
    return answer

# 초깃값은 -1이고 -1이 아닌 값인 경우는
# 각 칸에서 도착지까지 가는 경우를 기록해놓은 것임.
dfs_visited_dp = [[-1] * C for _ in range(R)]
def dfs(_coords, cr, cc):
    if cr == R - 1 and cc == C - 1:
        _coords[cr][cc] = 1
        return 1
    # cr, cc에서 도착지까지 가는 경우의 수
    answer = 0
    for dr, dc in drdc:
        nr, nc = cr + dr, cc + dc
        if 0 <= nr < R and 0 <= nc < C:
            if _coords[nr][nc] < _coords[cr][cc]:
                # 방문한 적 없는 지점이라면
                if dfs_visited_dp[nr][nc] == -1:
                    # print("처음 방문", nr, nc)
                    answer += dfs(_coords, nr, nc)
                elif 0 < dfs_visited_dp[nr][nc]:
                    # print("메모 이용", nr, nc, dfs_visited_dp[nr][nc])
                    answer += dfs_visited_dp[nr][nc]
                # 0인 경우는 해답이 없는 길인 경우
                else:
                    pass
    dfs_visited_dp[cr][cc] = answer
    return answer
# print(bfs(coords))
print(dfs(coords, 0, 0))
