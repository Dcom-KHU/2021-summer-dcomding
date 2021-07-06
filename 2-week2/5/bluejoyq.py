def solution(arrows):
    #n = int(input())
    #arrows = list(map(int, input().split()))
    n = len(arrows)
    SIZE = 200002
    result = 0
    # 방이 생겼다는 것은 이미 들린 정점에 다시 들리는 것.
    # 한번 간선을 탐색할때 마다 1씩 코스트를 늘려서 처음 정점에 들리면 추가
    # 왔다갔다로 코스트 차가 2인 경우를 거르자.
    # 이미 방문한 정점에 도착(도형을 그리기까지)하기 전에
    # 한번이라도 새 정점을 탄적이 있는지를 체크하면 도형의 중복 여부를 체크 가능하다.
    
    nodes = {i:{} for i in range(SIZE)}
    # 방향의 실제 y,x 변동
    moves = [[-1,0], [-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1]]

    # 시작은 항상 가운데
    cur_y = SIZE // 2
    cur_x = SIZE // 2
    nodes[cur_y][cur_x] = 1

    # 한번이라도 빈 간선을 탔는가
    is_valid = False
    for i in range(n):
        cur_arrow = arrows[i]

        cur_y += moves[cur_arrow][0]
        cur_x += moves[cur_arrow][1]
        
        # 2번 이전에 왔는가?
        try:
            if nodes[cur_y][cur_x] < i and is_valid:
                result += 1
                is_valid = False
                print(cur_y,cur_x)
        except:
            is_valid = True
        nodes[cur_y][cur_x] = i + 2
    return result