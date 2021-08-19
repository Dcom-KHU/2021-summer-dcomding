from heapq import heappop, heappush
import sys
input = sys.stdin.readline
MAX = sys.maxsize
def solution():
    def sperate_input():
        return map(int,input().split())
    n,m,k,start,end = sperate_input()
    traps = list(sperate_input())
    for i in range(k):
        traps[i] -= 1
    roads = [[MAX] * n for i in range(n)]
    for i in range(m):
        p,q,t = sperate_input()
        roads[p - 1][q - 1] = min(t, roads[p - 1][q - 1] )

    start -= 1
    end -= 1
    

    def exchange(target, idx):
        # 함정방을 위한 교환
        tmp = target[idx][:]
        for i in range(n):
            target[idx][i] = target[i][idx]
            target[i][idx] = tmp[i]
    # 함정방의 최대 개수가 10개이므로 비트마스크를 써야함.
    # road를 각 함정방의 경우에 수의 따라 다 만들어 놓자.
    # 최대가 3000 * 1000 = 3백만
    bit_max = pow(2,k)
    bit_check = [pow(2, i) for i in range(k)]
    roads_by_trap = [0] * bit_max
    for i in range(bit_max):
        roads_by_trap[i] = [road[:] for road in roads]

        for j in range(k):
            check = bit_check[j]
            if check & i == 0:
                continue
            idx = traps[j]
            exchange(roads_by_trap[i], idx)
    visited = [[0] * n for i in range(bit_max)]
    findings = []
    # cost, cur_pos, bit_idx
    heappush(findings, (0, start, 0))

    while findings:
        cur_cost, cur_pos, bit_idx = heappop(findings)
        if visited[bit_idx][cur_pos]:
            continue
        # 종결 조건
        if cur_pos == end:
            return cur_cost
        visited[bit_idx][cur_pos] = 1
        cur_road = roads_by_trap[bit_idx][cur_pos]
        for nxt_pos in range(n):
            cost = cur_road[nxt_pos]
            if cost == MAX:
                continue
            
            if nxt_pos in traps:
                new_bit_idx = bit_idx ^ (1 << traps.index(nxt_pos))
                if visited[new_bit_idx][nxt_pos]:
                    continue
                heappush(findings, (cur_cost + cost, nxt_pos, new_bit_idx))
            else:
                if visited[bit_idx][nxt_pos]:
                    continue
                heappush(findings, (cur_cost + cost, nxt_pos, bit_idx))
    
print(solution())