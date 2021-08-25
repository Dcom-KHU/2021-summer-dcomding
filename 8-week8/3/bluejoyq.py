def solution():
    from heapq import heappop, heappush
    import sys

    input = sys.stdin.readline
    MAX = sys.maxsize
    n,m,k,start,end = map(int,input().split())
    traps = list(map(int,input().split()))
    trap_checker = [-1] * (n + 1)
    for i in range(k):
        trap_checker[traps[i]] = i

    roads = {i:{} for i in range(1,n + 1) }
    reversed_roads = {i:{} for i in range(1,n + 1) }
    for i in range(m):
        p,q,t = map(int,input().split())
        try:
            roads[p][q] = min(t, roads[p][q] )
            reversed_roads[q][p] = min(t, reversed_roads[q][p] )
        except:
            roads[p][q] = t
            reversed_roads[q][p] = t
    # 함정방의 최대 개수가 10개이므로 비트마스크를 써야함.
    # road를 각 함정방의 경우에 수의 따라 다 만들어 놓자. -> 시간 초과의 원인이 이거네
    # 최대가 3000 * 1000 = 3백만
    bit_max = pow(2,k)
    bit_check = [pow(2, i) for i in range(k)]

    visited = [[0] * (n + 1) for i in range(bit_max)]
    findings = []

    # cost, cur_pos, bit_idx
    heappush(findings, (0, start, 0))

    def visit(bit_idx, cur_cost,nxt_pos, cost):
        # 다음 길이 트랩이라면
        if trap_checker[nxt_pos] != -1:
            new_bit_idx = bit_idx ^ bit_check[trap_checker[nxt_pos]]
            if visited[new_bit_idx][nxt_pos]:
                return
            heappush(findings, (cur_cost + cost, nxt_pos, new_bit_idx))
        else:
            if visited[bit_idx][nxt_pos]:
                return
            heappush(findings, (cur_cost + cost, nxt_pos, bit_idx))
    
    def is_reversed(bit_idx,pos):
        if trap_checker[pos] != -1 and bit_idx & bit_check[trap_checker[pos]]:
            return True
        return False
    while findings:

        cur_cost, cur_pos, bit_idx = heappop(findings)
        if visited[bit_idx][cur_pos]:
            continue
        # 종결 조건
        if cur_pos == end:
            return cur_cost
        visited[bit_idx][cur_pos] = 1

        # 이번이 거꾸로 되있다면.
        if trap_checker[cur_pos] != -1 and bit_idx & bit_check[trap_checker[cur_pos]]:
            # 역방향 간선들에 대해
            for nxt_pos in reversed_roads[cur_pos].keys():
                cost = reversed_roads[cur_pos][nxt_pos]
                if is_reversed(bit_idx,nxt_pos):
                    continue
                visit(bit_idx, cur_cost,nxt_pos, cost)
            
            # 역방항에서 정방향 간선으로 갈 수 있는 경우는 얘네가 함정인 경우 뿐

            for nxt_pos in traps:
                try:
                    cost = roads[cur_pos][nxt_pos]
                    if bit_idx & bit_check[trap_checker[nxt_pos]]:
                        visit(bit_idx, cur_cost,nxt_pos, cost)
                except:
                    continue
        else: # 여기가 정방향이면
            for nxt_pos in roads[cur_pos].keys():
                cost = roads[cur_pos][nxt_pos]
                if is_reversed(bit_idx,nxt_pos):
                    continue
                visit(bit_idx, cur_cost,nxt_pos, cost)
            for nxt_pos in traps:
                try:
                    cost = reversed_roads[cur_pos][nxt_pos]
                    if bit_idx & bit_check[trap_checker[nxt_pos]]:
                        visit(bit_idx, cur_cost,nxt_pos, cost)
                except:
                    continue
    return -1
print(solution())