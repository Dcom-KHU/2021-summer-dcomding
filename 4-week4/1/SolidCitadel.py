n, k = map(int, input().split())
moves = list(map(int, input().split()))
board = [list(r) for r in zip(*[map(int, input().split()) for i in range(n)])]
bucket = list()
result = 0

for m in moves:
    for i, p in enumerate(board[m-1]):
        if p:
            if bucket and bucket[-1] == p:
                bucket.pop()
                result += 2
            else:
                bucket.append(p)
            board[m-1][i] = 0
            break

print(result)
