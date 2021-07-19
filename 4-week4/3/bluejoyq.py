
def solution():
    n = int(input())
    
    # 벽을 그냥 방문 체크로 때려버린다.
    visited = [[[0,0] for i in range(n)] for j in range(n)]
    for i in range(n):
        tmp = list(map(int, input().split()))
        for j in range(n):
            if tmp[j]:
                visited[i][j] = [2,2]
            
    visited[0][0][0] = 1
    visited[0][1][1] = 2
    
    
    moves = [[0,1], [1,0], [-1,0], [0,-1]]
    rotates = [[[-1,0], [1,0]], [[0,-1], [0,1]]]
    goal = [n-1,n-1]
    
    def d2_shape_sum(a,b):
        return [a[0] + b[0], a[1] + b[1]] 

    def not_valid(a,b):
        if -1 < a[0] < n and  -1 < a[1] < n and -1< b[0] < n and -1< b[1] < n :
            if visited[a[0]][a[1]][0] and visited[b[0]][b[1]][1]:
                return 1 
            else:
                return 0
        return 1
    def not_valid_for_rotate(a,b):
        if -1 < a[0] < n and  -1 < a[1] < n and -1< b[0] < n and -1< b[1] < n and not (visited[b[0]][b[1]][1] == 2):
            if visited[a[0]][a[1]][0]:
                return 1 
            else:
                return 0
        return 1
    # shape : - 0 l 1
    findings = [[[0,0], [0,1],0]]
    for i in range(1, 101240):
        # 요주의 구간 deepcopy?
        nxt_findings = []
        while findings:
            cur_a, cur_b, shape = findings.pop()
            # 이동 가능한 곳이 있다면 이동 처리
            for move in moves:
                nxt_a = d2_shape_sum(cur_a,move)
                nxt_b = d2_shape_sum(cur_b,move)
                if not_valid(nxt_a, nxt_b):
                    continue
                if nxt_a == goal or nxt_b == goal:
                    return i 
                visited[nxt_a[0]][nxt_a[1]][0] = 1
                visited[nxt_b[0]][nxt_b[1]][1] = 1
                nxt_findings.append([nxt_a, nxt_b, shape])
                
            # 회전 가능한 곳이 있다면 회전 처리
            for rotate in rotates[shape]:
                nxt_a = d2_shape_sum(cur_a,rotate)
                nxt_a_final = d2_shape_sum(cur_b,rotate)
                if not_valid_for_rotate(nxt_a, nxt_a_final):
                    continue
                if nxt_a == goal or nxt_a_final == goal:
                    return i 
                visited[nxt_a_final[0]][nxt_a_final[1]][0] = 1
                nxt_findings.append([nxt_a_final, cur_b, 1 - shape])
            
            for rotate in rotates[shape]:
                nxt_b = d2_shape_sum(cur_b,rotate)
                nxt_b_final = d2_shape_sum(cur_a,rotate)
                if not_valid_for_rotate(nxt_b, nxt_b_final):
                    continue
                if nxt_b == goal or nxt_b_final == goal:
                    return i 
                visited[nxt_b_final[0]][nxt_b_final[1]][1] = 1
                nxt_findings.append([cur_a, nxt_b_final, 1 - shape])
        findings = nxt_findings
print(solution())