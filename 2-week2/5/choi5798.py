# 방이 생겼다는 것은 이미 들린 정점에 다시 들리는 것.
# 한번 간선을 탐색할때마다 1씩 코스트를 늘려서 처음 정점에 들리면 추가
# 왔다갔다로 코스트 차가 2인 경우를 거르자
# 이미 방문한 정점에 도착(도형을 그리기까지)하기 전에
# 한번이라도 정점에서의 새 edge를 탄적이 있는지를 체크하면 도형의 중복 여부를 체크 가능
from collections import defaultdict
from collections import deque
def solution(arrows):
    answer = 0
    node = defaultdict(int)
    now = (0,0)
    before = (0,0)
    edge = defaultdict(int)
    queue = deque([now])
    for com in arrows:
        if com == 0:
            dx = 0
            dy = 1
        elif com == 1:
            dx = 1
            dy = 1
        elif com == 2:
            dx = 1
            dy = 0
        elif com == 3:
            dx = 1
            dy = -1
        elif com == 4:
            dx = 0
            dy = -1
        elif com == 5:
            dx = -1
            dy = -1
        elif com == 6:
            dx = -1
            dy = 0
        elif com == 7:
            dx = -1
            dy = 1
        
        for i in range(2): # 점이 없는 곳에서 교차하는 경우(ex.모래시계모양)를 위해 점을 2개씩 찍기
            temp = (before[0]+dx, before[1]+dy)
            queue.append(temp)
            before = temp
        before = queue.popleft()
        node[before] = 1
        while queue:
            now = queue.popleft()
            if node[now] == 0: # 점에 처음 방문한 경우
                node[now] = 1 # 방문증 배부
            else: # 다시 방문한 경우!
                if edge[(before, now)] == 0: # 처음오는 길로 왔나요?
                    answer += 1
            edge[(before, now)] = 1
            edge[(now,before)] = 1
            before = now
        queue.append(before)
        
    return answer

n = int(input())
arrows = list(map(int, input().split()))
print(solution(arrows))