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
        time = len(set(map(tuple, moves)))
        print(time-2)
        break
    else:
        for dir in (not vertical, vertical), (-(not vertical),  -vertical):
            pos2 = (pos[0]+dir[0], pos[1]+dir[1])
            if pos2 not in moves and board[pos2] == 0:
                queue.append((moves+[pos2], vertical))
        for dir in (vertical, not vertical), (-vertical, -(not vertical)):
            pos2_ = (pos[0]+dir[0], pos[1]+dir[1])
            pos2__ = (pos0[0]+dir[0], pos0[1]+dir[1])
            if pos2_ not in moves and pos2__ not in moves and board[pos2_] + board[pos2__] == 0:
                queue.append((moves[:-1]+[list(pos), pos2_], not vertical))
                queue.append((moves[:-2]+[list(pos0), pos, pos2__], not vertical))
                queue.append((moves+[pos2_], vertical))
                queue.append((moves+[pos2__], vertical))
