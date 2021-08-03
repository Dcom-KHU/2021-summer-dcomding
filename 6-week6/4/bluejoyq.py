import sys
input = sys.stdin.readline
sys.setrecursionlimit(2000000)
def solution():
    N = int(input())
    values = list(map(int, input().split()))
    edges = {i:[] for i in range(N)}
    for i in range(N-1):
        a,b = map(int, input().split())
        edges[a].append(b)
        edges[b].append(a)
    # 모든 value의 합이 0이 아니면 무슨 짓을 해도 0으로 못만듬.
    if sum(values):
        return(-1)
    # 방향성이 없는 그래프이므로 간선이 1개인 node 아무거나 찾아서 root로 취급.
    for root in range(N):
        if len(edges[root]) == 1:
            break
    result = 0
    visited = [0 for i in range(N)]
    visited[root] = 1
    
    # 루트에서는 걍 아무 곳에나 더하게? 어차피 0이니까
    stk = [(root, root-1)] # 재귀 대신
    findings = [root]
    while findings:
        cur = findings.pop()
        
        for nxt in edges[cur]:
            if visited[nxt]:
                continue
            findings.append(nxt)
            visited[nxt] = 1
            stk.append((nxt, cur))
    
    for cur, parent in stk[::-1]:
        values[parent] += values[cur]
        result += abs(values[cur])
    
    return result
print(solution())