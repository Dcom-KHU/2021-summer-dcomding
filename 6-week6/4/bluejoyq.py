import sys
input = sys.stdin.readline
sys.setrecursionlimit(200000)
def solution():
    N = int(input())
    values = list(map(int, input().split()))
    edges = {i:[] for i in range(N)}
    for i in range(N-1):
        a,b = map(int, input().split())
        edges[a].append(b)
        edges[b].append(a)
    if sum(values):
        return(-1)
    # 방향성이 없는 그래프이므로 간선이 1개인 node 아무거나 찾아서 root로 취급.
    for root in range(N):
        if len(edges[root]) == 1:
            break
    global result
    result = 0
    visited = [0 for i in range(N)]
    visited[root] = 1
    stk = [] # 재귀 대신
    
    def recur_make_zero(cur, visited, values,edges):
        global result
        for nxt in edges[cur]:
            if visited[nxt]:
                continue
            visited[nxt] = 1
            recur_make_zero(nxt, visited, values,edges)
            values[cur] += values[nxt]
            result += abs(values[nxt])
    recur_make_zero(root, visited, values,edges)
    return result
print(solution())