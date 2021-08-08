n, m = map(int, input().split())
matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split())))


d = [[0 for i in range(m)] for j in range(n)]

def dfs(x, y):
    # if arrived
    if (x,y) == (n-1,m-1):
        return 1

    # if reached known route
    elif d[x][y] != 0:
        return d[x][y]

    else:
        # up
        if 0 <= x-1 and matrix[x-1][y] < matrix[x][y]:
            d[x][y] += dfs(x-1, y)

        # down
        if x+1 < n and matrix[x+1][y] < matrix[x][y]:
            d[x][y] += dfs(x+1, y)

        # left
        if 0 <= y-1 and matrix[x][y-1] < matrix[x][y]:
            d[x][y] += dfs(x, y-1)

        # right
        if y+1 < m and matrix[x][y+1] < matrix[x][y]:
            d[x][y] += dfs(x, y+1)

        return d[x][y]


print(dfs(0,0))
