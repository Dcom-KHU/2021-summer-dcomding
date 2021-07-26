import heapq
def solve():
    N = int(input())
    values = [0] * N
    for i in range(N):
        values[i] = tuple(map(int,input().split()))
    values.sort()
    
    # 현재 막힌 부분이 사용가능한 컴퓨터가 여러 대 있을 때
    # 이 중 idx가 가장 빠른 pc에 접근해야함.
    
    # heapq에 다 넣어서 끝나는 시간상 최소를 뽑고
    # 최소가 현재 시작 시간보다 크다면? (못넣으면)
    # 새로 idx 추가하고 현재꺼를 새로 집어넣고,
    # 만약 작다면 계속 뽑아서 can_add_idx heapq에 추가하고.
    # 그 중 제일 작은거를 뽑아서 추가! logN이 여러번이니까 ㄱㅊ을듯
    
    end_que = []
    idx_que = []
    cache = [0] * N
    nxt_idx = 0
    
    for start,end in values:
        if len(idx_que):
            idx = heapq.heappop(idx_que)
            cache[idx] += 1
            heapq.heappush(end_que, (end, idx))
        elif len(end_que):
            fastest_end, fastest_idx = end_que[0]
            if fastest_end <= start:
                try:
                    while fastest_end <= start:
                        f_end, f_idx = heapq.heappop(end_que)
                        heapq.heappush(idx_que, f_idx)
                        fastest_end, fastest_idx = end_que[0]
                except:
                    pass
                idx = heapq.heappop(idx_que)
                cache[idx] += 1
                heapq.heappush(end_que, (end, idx))
            else:
                cache[nxt_idx] += 1
                heapq.heappush(end_que, (end, nxt_idx))
                nxt_idx += 1
        else:
            cache[nxt_idx] += 1
            heapq.heappush(end_que, (end, nxt_idx))
            nxt_idx += 1
            
    print(nxt_idx)
    print(*cache[:nxt_idx])
solve()

'''
5
0 10
10 20
20 30
30 40
40 50
'''