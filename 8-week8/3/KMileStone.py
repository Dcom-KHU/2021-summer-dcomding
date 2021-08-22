import heapq

n, m, k, start, end = map(int, input().split())
traps = list(map(int, input().split()))
roads = {}
for i in range(m):
    u, v, cost = map(int, input().split())
    roads.setdefault(u, [])
    roads[u].append((v, cost, 0))
    roads.setdefault(v, [])
    roads[v].append((u, cost, 1))


d = [[float('inf') for i in range(2 * max(len(p) for p in roads.values()) + 1)] for j in range(n+1)]
d[start] = [0 for i in range(len(d[0]))]
heap = [(0, start)]
visit = [0 for i in range(n+1)]

# dijkstra
while heap:
    cursor = heapq.heappop(heap)[1]

    if visit[cursor] < len(roads.get(cursor)) or (visit[cursor] < 2 * len(roads.get(cursor)) and cursor in traps):
        visit[cursor] += 1

        path = roads.get(cursor)
        if path:
            for dst, cost, dir in path:
                trapped = 0
                if cursor in traps:
                    trapped += visit[cursor]
                if dst in traps:
                    trapped += visit[dst]
                trapped %= 2

                # if trapped, reverse dir (1)
                # if not trapped, forward dir (0)
                if trapped == dir:
                    heapq.heappush(heap, (cost*3000 + visit[dst], dst))
                    d[dst][visit[dst]] = min(d[dst][visit[dst]], d[cursor][visit[cursor]-1] + cost)


if d[end][0] == float('inf'):
    print(-1)
else:
    print(d[end][0])
