n = int(input())
list_var = list(map(int, input().split()))
set_var = {(0, 0)}
edge_var = set()

dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [1, 1, 0, -1, -1, -1, 0, 1]

count = 0
current = [0, 0]

for depth in range(n):
    nx = dx[list_var[depth]]
    ny = dy[list_var[depth]]

    first = tuple(sorted([(current[0], current[1]), (current[0] + nx, current[1] + ny)]))
    second = tuple(sorted([(current[0] + nx, current[1] + ny), (current[0] + 2 * nx, current[1] + 2 * ny)]))

    current[0] += nx
    current[1] += ny

    if first not in edge_var:
        edge_var.add(first)
        if tuple(current) in set_var:
            count += 1
        else:
            set_var.add(tuple(current))
    
    current[0] += nx
    current[1] += ny

    if second not in edge_var:
        edge_var.add(second)
        if tuple(current) in set_var:
            count += 1
        else:
            set_var.add(tuple(current))
    
print(count)