n, m = map(int, input().split())
matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split())))


d = [[0 for i in range(m)] for j in range(n)]
d[n-1][m-1] = 1

# recursive to stack
stack = [(0, 0, -1, -1)]

while stack:
    (x, y, prev_x, prev_y) = stack.pop()

    # if reached known route or returning
    if d[x][y] != 0:
        d[prev_x][prev_y] += d[x][y]

    else:
        # return point
        stack.append((x, y, prev_x, prev_y))

        # up
        if 0 <= x-1 and matrix[x-1][y] < matrix[x][y]:
            stack.append((x-1, y, x, y))

        # down
        if x+1 < n and matrix[x+1][y] < matrix[x][y]:
            stack.append((x+1, y, x, y))

        # left
        if 0 <= y-1 and matrix[x][y-1] < matrix[x][y]:
            stack.append((x, y-1, x, y))

        # right
        if y+1 < m and matrix[x][y+1] < matrix[x][y]:
            stack.append((x, y+1, x, y))


print(d[0][0])
