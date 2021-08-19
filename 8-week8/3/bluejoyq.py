from heapq import heappop, heappush
import sys
# import time
# import random

# def decorator(func):   
    
#     def wrapper(*args, **kwargs):   
#         bef = time.time() 
#         result = func(*args, **kwargs)        
#         aft = time.time()
#         print(aft - bef)
#         return result
    
#     return wrapper               

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
    
    visited = [0] * (n + 1) 
    # n = 1000
    # m = 3000
    # k = 10
    # start, end = 1, 1000
    # roads = [[MAX] * (n + 1) for i in range(n + 1)]
    # traps = [random.randint(2,999) for i in range(k)]
    # trap_checker = [-1] * (n + 1)
    # for i in range(k):
    #     trap_checker[traps[i]] = i

    # for i in range(m):
    #     p,q,t = random.randint(1,1000), random.randint(1,1000), random.randint(1,3000)
    #     roads[p][q] = min(t, roads[p][q] )
    # roads[1][1000] = 3000 * 3000
    def exchange(target, idx):
        # 함정방을 위한 교환
        tmp = target[idx][:]
        for i in range(n + 1):
            target[idx][i] = target[i][idx]
            target[i][idx] = tmp[i]
    
    def is_visited(cur_pos, bit_idx):
        if trap_checker[cur_pos] != -1:
            activated= int(bool( bit_idx  & (1 << trap_checker[cur_pos])))
            if visited[cur_pos][activated]:
                return 1
        else:
            if visited[cur_pos]:
                return 1
        return 0

    def visit(cur_pos, bit_idx):
        if trap_checker[cur_pos] != -1:
            activated=int(bool( bit_idx  & (1 << trap_checker[cur_pos])))
            visited[cur_pos][activated] = 1
        else:
            visited[cur_pos] = 1

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
    
    for trap in traps:
        visited[trap] = [0,0]
    findings = []
    # cost, cur_pos, bit_idx
    heappush(findings, (0, start, 0))

    while findings:
        cur_cost, cur_pos, bit_idx = heappop(findings)
        if is_visited(cur_pos, bit_idx):
            continue
        # 종결 조건
        if cur_pos == end:
            return cur_cost
        visit(cur_pos, bit_idx)
        cur_road = roads_by_trap[bit_idx][cur_pos]
        for nxt_pos in range(1, n + 1):
            cost = cur_road[nxt_pos]
            if cost == MAX:
                continue
            
            if trap_checker[nxt_pos] != -1:
                new_bit_idx = bit_idx ^ (1 << trap_checker[nxt_pos])
                if is_visited(nxt_pos, new_bit_idx):
                    continue
                heappush(findings, (cur_cost + cost, nxt_pos, new_bit_idx))
            else:
                if is_visited(nxt_pos, bit_idx):
                    continue
                heappush(findings, (cur_cost + cost, nxt_pos, bit_idx))
    
print(solution())