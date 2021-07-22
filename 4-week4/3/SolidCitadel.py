from collections import deque

n = int(input())
board = {(x+1, y+1): int(p) for y in range(n) for x, p in enumerate(input().split())}
for x in range(n+2):
    for y in [0, n+1]:
        board[x, y] = 1
        board[y, x] = 1
queue = deque([ ([(1, 1), (2, 1)], False) ])

while queue:
    moves, vertical = queue.popleft()
    pos = moves[-1]
    pos0 = moves[-2]
    if pos == (n, n):
        time = 0
        for i in range(len(moves)-1):
            time += min([abs(moves[i][0]-m[0]) + abs(moves[i][1]-m[1]) for m in moves[i+1:]])
        print(time-1)
        break
    else:
        for dir in (not vertical, vertical), (-(not vertical),  -vertical):
            pos2 = (pos[0]+dir[0], pos[1]+dir[1])
            if pos2 not in moves and board[pos2] == 0:
                queue.append((moves+[pos2], vertical))
        for dir in (vertical, not vertical), (-vertical, -(not vertical)):
            pos2 = (pos[0]+dir[0], pos[1]+dir[1])
            if pos2 not in moves and board[pos2] + board[pos0[0], pos2[1]] + board[pos2[0], pos0[1]] == 0:
                moves[-1] = pos2
                queue.append((moves[:], not vertical))
