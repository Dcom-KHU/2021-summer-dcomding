from copy import deepcopy
n = int(input(""))
directions = list(map(int, input("").split()))

new = True
now = [0, 0]
visited = []
visited.append(deepcopy(now))
shapes = 0

for d in directions:
    if d == 0:
        now[1] += 1
    elif d == 1:
        now[0] += 1
        now[1] += 1
    elif d == 2:
        now[0] += 1
    elif d == 3:
        now[0] += 1
        now[1] -= 1
    elif d == 4:
        now[1] -= 1
    elif d == 5:
        now[0] -= 1
        now[1] -= 1
    elif d == 6:
        now[0] -= 1
    elif d == 7:
        now[0] -= 1
        now[1] += 1
    if now in visited:
        if new:
            shapes += 1
        new = False
    else:
        visited.append(deepcopy(now))
        new = True

print(shapes)