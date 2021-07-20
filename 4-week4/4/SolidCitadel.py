N, L = map(int, input().split())
board = [list(map(int, input().split())) for i in range(N)]

count = N*2
for way in board + [[board[j][i] for j in range(N)] for i in range(N)]:
    height = way[0]
    for i, h in enumerate(way):
        if 2 <= abs(height-h):
            count -= 1
            break
        elif 1 <= abs(height - h):
            if h < height and i+L <= N and set(way[i:i+L]) == {h}:
                height -= 1
                way[i:i+L] = [h+0.5]*L
            elif h > height and i-L >= 0 and set(way[i-L:i]) == {height}:
                height += 1
                way[i-L:i] = [h-0.5]*L
            else:
                count -= 1
                break

print(count)
