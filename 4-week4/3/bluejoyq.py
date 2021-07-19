def solution():
    n = int(input())
    board = [0] * n
    # 벽을 그냥 방문 체크로 때려버린다.
    
    for i in range(n):
        board[i] = list(map(int, input().split()))
    visited = [[[0,0] for i in range(n)] for j in range(n)]
    # y, x, shape
    visited[0][0][0] = 1
    visited[0][1][0] = 1
    moves = [[0,1], [1,0], [-1,0], [0,-1]]
    rotates = [[[-1,0], [1,0]], [[0,-1], [0,1]]]
    goal = [n-1,n-1]

    def d2_shape_sum(a,b):
        return [a[0] + b[0], a[1] + b[1]]
    
    def not_valid(a,b, shape):
        if -1 < a[0] < n and  -1 < a[1] < n and -1< b[0] < n and -1< b[1] < n :
            if board[a[0]][a[1]] or board[b[0]][b[1]]:
                return 1
            elif visited[a[0]][a[1]][shape] and visited[b[0]][b[1]][shape]:
                return 1
            return 0
        return 1

    def not_valid_for_rotate(tmp_a,a, shape):
        if -1 < tmp_a[0] < n and  -1 < tmp_a[1] < n and -1< a[0] < n and -1< a[1] < n:
            # 지나가는 쪽에 벽이 있거나
            if board[tmp_a[0]][tmp_a[1]] or board[a[0]][a[1]] or (visited[a[0]][a[1]][shape] ):
                return 1
            else:
                return 0
        return 1

    # shape : - 0 l 1
    findings = [[[0,0], [0,1],0]]
    for i in range(1, 101240):
        nxt_findings = []
        while findings:
            cur_a, cur_b, cur_shape = findings.pop()
            # print(cur_a, cur_b,cur_shape, i, findings,"///", visited)
            # 이동 가능한 곳이 있다면 이동 처리
            for move in moves:
                nxt_a = d2_shape_sum(cur_a,move)
                nxt_b = d2_shape_sum(cur_b,move)
                if not_valid(nxt_a, nxt_b, cur_shape):
                    continue
                if nxt_a == goal or nxt_b == goal:
                    return i
                visited[nxt_a[0]][nxt_a[1]][cur_shape] = 1
                visited[nxt_b[0]][nxt_b[1]][cur_shape] = 1
                nxt_findings.append([nxt_a, nxt_b, cur_shape])

            
            # 회전 가능한 곳이 있다면 회전 처리
            nxt_shape =  1 - cur_shape
            for rotate in rotates[cur_shape]:
                nxt_a_tmp = d2_shape_sum(cur_a,rotate)
                nxt_a_final = d2_shape_sum(cur_b,rotate)
                
                if not_valid_for_rotate(nxt_a_tmp, nxt_a_final,nxt_shape):
                    continue
                if nxt_a_final == goal:
                    return i
                
                visited[cur_b[0]][cur_b[1]][nxt_shape] = 1
                visited[nxt_a_final[0]][nxt_a_final[1]][nxt_shape] = 1
                nxt_findings.append([nxt_a_final, cur_b,nxt_shape])
                
            for rotate in rotates[cur_shape]:
                nxt_b_tmp = d2_shape_sum(cur_b,rotate)
                nxt_b_final = d2_shape_sum(cur_a,rotate)
                
                if not_valid_for_rotate(nxt_b_tmp, nxt_b_final,nxt_shape):
                    continue
                if nxt_b_final == goal:
                    return i
                
                visited[cur_a[0]][cur_a[1]][nxt_shape] = 1
                visited[nxt_b_final[0]][nxt_b_final[1]][nxt_shape] = 1
                nxt_findings.append([cur_a, nxt_b_final,nxt_shape])
        
            
        findings = nxt_findings
    return 0
print(solution())