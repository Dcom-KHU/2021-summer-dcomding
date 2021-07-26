import heapq
def solve():
    N = int(input())
    
    # 시작 시간이 빠른 순서대로 들어가니까 sort
    values = [0] * N
    for i in range(N):
        values[i] = tuple(map(int,input().split()))
    
    values.sort()
    
    que = []
    cache = [0] * N
    fastest_end = 9876543210
    fastest_idx = 0
    nxt_idx = 0
    
    for start,end in values:
        # case1: 가장 빨리 끝나는 시간보다 빠르다면 가장 빠른 끝나는 시간을 갱신하고
        # 기존 종료 시간은 que에 넣는다.
        if end < fastest_end:
            heapq.heappush(que, (fastest_end, fastest_idx))
            fastest_end = end
            fastest_idx = nxt_idx
            cache[nxt_idx] += 1
            nxt_idx += 1
        # case2: 가장 빨리 끝나는 시간보다 시작이 빠르다면 (즉 이어서 할 수 없다면)
        # 새 종료 시간을 que에 넣는다.
        elif start < fastest_end:
            heapq.heappush(que, (end, nxt_idx))
            cache[nxt_idx] += 1
            nxt_idx += 1
        # case3: 가장 빨리 끝나는 시간보다 시작이 느리거나 같다면 (즉 이어서 이용 가능하다면)
        # 현재 종료 시간을 que에 넣고 새로운 최단 종료 시간을 que로부터 받는다.
        else:
            heapq.heappush(que, (end, fastest_idx))
            cache[fastest_idx] += 1
            fastest_end, fastest_idx = heapq.heappop(que)
    print(nxt_idx)
    print(*cache[:nxt_idx])
solve()
