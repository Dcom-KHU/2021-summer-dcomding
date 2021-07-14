import heapq
def solve():
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for i in range(N)]
    
    # 일단 이 보드를 그래프로 모델링해야함.
    # 모든 블럭을 돌면서 라벨링부터 하자.
    # 각 섬에 번호를 붙여주는거임.
    searchs = [[-1,0], [0,1], [1,0], [0,-1]]
    cur_numbering = 1
    visited = [[0 for j in range(M)] for i in range(N)]
    
    islands = []
    for y in range(N):
        for x in range(M):
            if not board[y][x] or visited[y][x]:
                continue
            # 처음 해당 섬에 도달하면 그 섬 좌표 기록하고 dfs
            board[y][x] = cur_numbering
            islands.append((y,x))
            
            visited[y][x] = 1           
            findings= [(y,x)]
            while findings:
                cur_y, cur_x = findings.pop()
                for search in searchs:
                    nxt_y, nxt_x = cur_y + search[0], cur_x + search[1]
                    if (-1 < nxt_y < N) and (-1 <nxt_x < M) and not visited[nxt_y][nxt_x] and board[nxt_y][nxt_x]:
                        findings.append((nxt_y, nxt_x))
                        visited[nxt_y][nxt_x] = 1
                        board[nxt_y][nxt_x] = cur_numbering
                    
            cur_numbering += 1
    goal = len(islands)
    edges = {i+1 : [] for i in range(goal)}
    visited = [[0 for j in range(M)] for i in range(N)]
    for idx in range(goal):
        y, x = islands[idx]
        visited[y][x] = 1
        findings= [(y, x)]
        while findings:
            cur_y, cur_x = findings.pop()
            for search in searchs:
                nxt_y, nxt_x = cur_y + search[0], cur_x + search[1]
                if (-1 < nxt_y < N) and (-1 <nxt_x < M) and not visited[nxt_y][nxt_x]:
                    if board[nxt_y][nxt_x]:
                        findings.append((nxt_y, nxt_x))
                        visited[nxt_y][nxt_x] = 1
                    else:
                        length = 0
                        while (-1 < nxt_y < N) and (-1 <nxt_x < M):
                            if board[nxt_y][nxt_x]:
                                break
                            nxt_y += search[0]
                            nxt_x += search[1]
                            length += 1
                            
                                
                        if length > 1 and (-1 < nxt_y < N) and (-1 <nxt_x < M):
                            # 목적지, 코스트
                            edges[idx+1].append((board[nxt_y][nxt_x], length))
    
    goal_bit = (1 << goal) - 1
    findings = []

    heapq.heappush(findings, (0,1))
    try:
        while True:
            cur_cost, has_been = heapq.heappop(findings)
            if has_been == goal_bit:
                print(cur_cost)
                break
            for i in range(goal):
                if not ((1 << i) & has_been):
                    continue
                for nxt, nxt_cost in edges[i+1]:
                    if (1 << (nxt - 1)) & has_been:
                        continue
                    heapq.heappush(findings, (cur_cost + nxt_cost, (1 << (nxt - 1)) | has_been))
    except:
        print(-1)
solve()