n, k = map(int, input().split())
moves = list(map(int, input().split()))
board = []
for i in range(n):
    board.append(list(map(int, input().split())))


bascket = []
count = 0

for m in moves:
    # draw doll
    for i in range(n):
        if board[i][m-1] != 0:
            bascket.append(board[i][m-1])
            board[i][m-1] = 0
            break

    # check prize
    if len(bascket) > 1 and bascket[-1] == bascket[-2]:
        bascket.pop()
        bascket.pop()
        count += 2

print(count)
