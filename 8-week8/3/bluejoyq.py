from heapq import heappop, heappush
import sys

input = sys.stdin.readline
MAX = sys.maxsize
def solution():
    def sperate_input():
        return map(int,input().split())
    n,m,k,start,end = sperate_input()
    traps = list(sperate_input())
    trap_checker = [-1] * (n + 1)
    for i in range(k):
        trap_checker[traps[i]] = i

    roads = [[MAX] * (n + 1) for i in range(n + 1)]
    for i in range(m):
        p,q,t = sperate_input()
        roads[p][q] = min(t, roads[p][q] )
    
    # 함정방의 최대 개수가 10개이므로 비트마스크를 써야함.
    # road를 각 함정방의 경우에 수의 따라 다 만들어 놓자. -> 시간 초과의 원인이 이거네 ㅅㅂ
    # 최대가 3000 * 1000 = 3백만
    bit_max = pow(2,k)
    bit_check = [pow(2, i) for i in range(k)]

    visited = [[0] * (n + 1) for i in range(bit_max)]
    findings = []

    # cost, cur_pos, bit_idx
    heappush(findings, (0, start, 0))

    def visit(bit_idx, cur_cost,cur_pos,nxt_pos, cost):
        if cost == MAX:
            return
        # 다음 길이 트랩이라면
        if trap_checker[nxt_pos] != -1:
            if bit_idx & bit_check[trap_checker[nxt_pos]] and roads[nxt_pos][cur_pos] == MAX:
                return
            new_bit_idx = bit_idx ^ bit_check[trap_checker[nxt_pos]]
            if visited[new_bit_idx][nxt_pos]:
                return
            heappush(findings, (cur_cost + cost, nxt_pos, new_bit_idx))
        else:
            if visited[bit_idx][nxt_pos]:
                return
            heappush(findings, (cur_cost + cost, nxt_pos, bit_idx))
    while findings:
        #print(findings)
        #print(findings)
        cur_cost, cur_pos, bit_idx = heappop(findings)
        if visited[bit_idx][cur_pos]:
            continue
        # 종결 조건
        if cur_pos == end:
            return cur_cost
        visited[bit_idx][cur_pos] = 1
        #print(cur_pos,trap_checker[cur_pos], bit_check[trap_checker[cur_pos]], bit_idx)
        # 이번이 거꾸로 되있다면.
        if trap_checker[cur_pos] != -1 and bit_idx & bit_check[trap_checker[cur_pos]]:
            for nxt_pos in range(1, n + 1):
                cost = roads[nxt_pos][cur_pos]
                if cost == MAX:
                    continue
                # 다음 길이 트랩이라면
                if trap_checker[nxt_pos] != -1:
                    if bit_idx & bit_check[trap_checker[nxt_pos]] and roads[nxt_pos][cur_pos] == MAX:
                        continue
                    new_bit_idx = bit_idx ^ bit_check[trap_checker[nxt_pos]]
                    if visited[new_bit_idx][nxt_pos]:
                        continue
                    heappush(findings, (cur_cost + cost, nxt_pos, new_bit_idx))
                else:
                    if visited[bit_idx][nxt_pos]:
                        continue
                    heappush(findings, (cur_cost + cost, nxt_pos, bit_idx))
            for nxt_pos in range(1, n + 1):
                cost = roads[cur_pos][nxt_pos]
                if cost == MAX:
                    continue
                if trap_checker[nxt_pos] != -1 and bit_idx & bit_check[trap_checker[nxt_pos]]:
                    new_bit_idx = bit_idx ^ bit_check[trap_checker[nxt_pos]]
                    if visited[new_bit_idx][nxt_pos]:
                        continue
                    heappush(findings, (cur_cost + cost, nxt_pos, new_bit_idx))
        else:
            for nxt_pos in range(1, n + 1):
                cost = roads[cur_pos][nxt_pos]
                visit(bit_idx, cur_cost,cur_pos,nxt_pos, cost)
            for nxt_pos in range(1, n + 1):
                cost = roads[nxt_pos][cur_pos]
                if cost != MAX and trap_checker[nxt_pos] != -1 and bit_idx & bit_check[trap_checker[nxt_pos]]:
                    visit(bit_idx, cur_cost,cur_pos,nxt_pos, cost)
print(solution())