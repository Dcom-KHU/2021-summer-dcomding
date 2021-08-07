n, m = map(int, input().split())
board = {(x+1, y+1): int(p) for y in range(n) for x, p in enumerate(input().split())}

dp = {k: None for k in board.keys()} #None: 미방문, int: 해당 위치에서 종점까지 가능한 경로의 수
dp[m, n] = 1

#벽
for x in [0, m+1]:
    for y in range(n+2):
        board[x, y] = float('inf')
for y in [0, n+1]:
    for x in range(1, m+1):
        board[x, y] = float('inf')

stack = [[(1, 1)]]
while stack:
    route = stack.pop()
    pos = route[-1]
    dp[pos] = 0
    for x, y in (1, 0), (0, 1), (-1, 0), (0, -1):
        npos = (pos[0]+x, pos[1]+y)
        if board[npos] < board[pos]:
            if dp[npos]: #not None and not 0
                for p in route:
                    dp[p] += dp[npos]
            elif dp[npos] == None:
                stack.append(route+[npos])

print(dp[1, 1])
