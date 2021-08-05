import sys
sys.setrecursionlimit(20000)
input = sys.stdin.readline
n, m = map(int, input().split())
map_val = []
for _ in range(n):
    temp = list(map(int, input().split()))
    map_val.append(temp)

dxy = [(-1,0),(1,0),(0,-1),(0,1)] # 상, 하, 좌, 우
dp = [[-1 for _ in range(m)] for _ in range(n)]
#dp[y][x]: 점x,y에서 목적지(점m-1,n-1)까지 갈 수 있는 길의 수

def is_inside(y, x):
    return 0 <= y < n and 0 <= x < m


def dfs(y, x):
    if y == n-1 and x == m-1:
        return 1
    
    elif dp[y][x] == -1:
        dp[y][x] = 0
        for dy, dx in dxy:
            new_y, new_x = y+dy, x+dx
            if is_inside(new_y, new_x):
                if map_val[y][x] > map_val[new_y][new_x]:
                    # stack.append([new_y, new_x])
                    dp[y][x] += dfs(new_y, new_x)
    return dp[y][x]
    
#단순히 dfs로만 풀면 되는 문제인지 알고 호기롭게 덤볐다가
# 삽질을 열심히 하던 중 시간초과의 배후가 있다는 사실을 알고
#결국 dp가 필요하다는 도움을 받았고 생각보다 간단하게 풀렸다..
#dfs와 dp의 조합이 너무 신선했다



print(dfs(0, 0))