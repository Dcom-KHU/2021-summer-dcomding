n = int(input())
a = list(map(int, input().split()))
edges = {}
for i in range(n-1):
    u, v = map(int, input().split())
    edges.setdefault(u, [])
    edges[u].append(v)
    edges.setdefault(v, [])
    edges[v].append(u)


# recursive to stack
stack = [(0, -1)]
visited = [False for i in range(n)]
count = 0

# if sum of a is not 0, you cannot make 0 all
if sum(a) != 0:
    count = -1
else:
    while stack:
        (node, prev) = stack.pop()

        # if leaf node
        if len(edges[node]) == 1:
            count += abs(a[node])
            a[prev] += a[node]
            edges[prev].remove(node)

        elif not visited[node]:
            visited[node] = True

            # return point
            stack.append((node, prev))

            for next in edges[node]:
                stack.append((next, node))


print(count)
