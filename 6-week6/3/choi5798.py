from collections import deque
n, m = map(int, input().split())
map_val = []
for _ in range(n):
    temp = list(map(int, input().split()))
    map_val.append(temp)

dxy = [(-1,0),(1,0),(0,-1),(0,1)] # 상, 하, 좌, 우
route = deque()

# def is_inside(y, x):
#     return 0 <= y < n and 0 <= x < m

def get_new_route(y, x):
    new_route = []
    for dy, dx in dxy:
        new_y = y+dy
        new_x = x+dx
        # if is_inside(new_y, new_x):
        try:
            if map_val[y][x] > map_val[new_y][new_x]: # 내리막길인지?
                new_route.append([new_y, new_x])
        except:
            continue
    return new_route

def bfs(y, x):
    answer = 0
    route.append([y, x])
    while route:
        new_y, new_x = route.popleft()
        if new_y == n-1 and new_x == m-1:
            answer += 1
            continue
        new_route = get_new_route(new_y, new_x)
        route.extend(new_route)
        
    return answer

print(bfs(0, 0))