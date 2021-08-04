n = int(input())
A = list(map(int, input().split()))
weights = {}
edges = {}
answer = 0
visited = [False for _ in range(n)]
def dfs(index):
    global answer
    weight = weights[index]
    visited[index] = True
    for i in edges[index]:
        if visited[i] is False:
            weight += dfs(i)
    answer += abs(weight)

    return weight
    
for _ in range(n-1):
    i, j = map(int, input().split())
    if edges.get(i) is None:
        edges[i] = [j]
    else:
        edges[i].append(j)
    if edges.get(j) is None:
        edges[j] = [i]
    else:
        edges[j].append(i)

for i in range(n):
    weights[i] = A[i]

if sum(weights.values()) != 0: # 모두 0으로 만들 수 없을 때
    print(-1)
else:
    dfs(0)
    print(answer)



