from collections import deque
n = int(input())
board = [[1 for _ in range(n+1)]]
for _ in range(n):
    temp = [1]
    temp.extend((list(map(int, input().split()))))
    board.append(temp)
#index를 1~n만 사용, 0은 사용 x
start = [[1,1], [1,2]]
move = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 상, 하, 좌, 우
queue = deque() # datatype: [[현위치], 걸린 시간]
visited = []
def is_inside(x, y):
    if 1 <= x <= n and 1 <= y <= n:
        return True
    return False

def get_next_idx(now, time):
    time += 1
    next_list = []
    x1, y1 = now[0]
    x2, y2 = now[1]
    for dx, dy in move: # 상하좌우 이동
        new_1x, new_1y = x1+dx, y1+dy
        new_2x, new_2y = x2+dx, y2+dy
        if is_inside(new_1x, new_1y) and is_inside(new_2x, new_2y):
            if board[new_1x][new_1y] == 0 and board[new_2x][new_2y] == 0:
                next_list.append([[[new_1x, new_1y],[new_2x, new_2y]], time])
    
    if x1 == x2: # 가로 -> 세로
        for dx, dy in move[0:3]:
            if is_inside(x1+dx, y1) and is_inside(x2+dx, y2):
                if board[x1+dx][y1] == 0 and board[x2+dx][y2] == 0:
                    next_list.append([[[x1+dx, y1],[x1, y1]], time])
                    next_list.append([[[x2+dx, y2], [x2, y2]], time]) 
    else: # 세로 -> 가로
        for dx, dy in move[2:]:
            if is_inside(x1, y1+dy) and is_inside(x2, y2+dy):
                if board[x1][y1+dy] == 0 and board[x2][y2+dy] == 0:
                    next_list.append([[[x1, y1+dy],[x1, y1]], time])
                    next_list.append([[[x2, y2+dy], [x2, y2]], time])
    return next_list

def bfs(now):
    queue.append([now, 0])
    visited.append(now)
    while queue:
        now, time = queue.popleft()
        next_idx = get_next_idx(now, time)
        for box in next_idx:
            moving, time = box[0], box[1]
            if moving[0] == [n,n] or moving[1] == [n, n]:
                return time
            elif moving not in visited:
                queue.append([moving, time])
                visited.append(moving)

print(bfs(start))