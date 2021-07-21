N, L = map(int, input().split())
maps = []
blocks = [[False for _ in range(N)] for _ in range(N)]
answer = 0
for _ in range(N):
    temp = list(map(int, input().split()))
    maps.append(temp)

def check(i, mid, end):
    for j in range(mid, end):
        if blocks[i][j] is True:
            return False
    return True

def rotate(arr):
    arr_90 = []
    for j in range(N):
        temp = []
        for i in range(N):
            temp.append(arr[i][j])
        arr_90.append(temp)
    return arr_90

def godhand(i, j, switch, maps):
    if switch == 0: # 오르막길을 만났을 때
        try:
            godroad = set(maps[i][j-L:j])
            if len(godroad) == 1 and check(i, j-L, j):
                return True
            else:
                return False
        except:
            return False
    elif switch == 1: # 내리막길을 만났을 때
        try:
            godroad = set(maps[i][j:j+L])
            if len(godroad) == 1 and check(i, j, j+L):
                for idx in range(j,j+L):
                    blocks[i][idx] = True
                return True
            else:
                return False
        except:
            return False
        
def reset():
    return [[False for _ in range(N)] for _ in range(N)]

def ramp(maps):
    roads = 0
    for i in range(N):
        success = True
        for j in range(1, N):
            if maps[i][j] > maps[i][j-1]: # 올라갑니다
                if maps[i][j] - maps[i][j-1] == 1:
                    if godhand(i, j, 0, maps): # 오르막길을 경사로로 지나감
                        continue
                success = False
                break
            elif maps[i][j] < maps[i][j-1]: # 내려갑니다
                if maps[i][j-1] - maps[i][j] == 1:
                    if godhand(i, j, 1, maps): # 내리막길을 경사로로 지나감
                        continue
                success = False
                break
        if success:
            roads += 1
    return roads

maps_90 = rotate(maps)
#가로조사
answer += ramp(maps)
blocks = reset()
#세로 조사
answer += ramp(maps_90)

print(answer)
