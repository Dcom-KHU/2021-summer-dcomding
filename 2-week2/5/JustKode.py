n = int(input())
list_var = list(map(int, input().split()))
set_var = {(0, 0), }

dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [1, 1, 0, -1, -1, -1, 0, 1]

count = 0
current = [0, 0]

def dfs(depth):
    global current
    global count
    
    print(set_var)

    if depth == n:
        return

    current[0] += dx[list_var[depth]]
    current[1] += dy[list_var[depth]]

    if tuple(current) in set_var:
        count += 1
    else:
        set_var.add(tuple(current))
    
    dfs(depth + 1)

dfs(0)
print(count)