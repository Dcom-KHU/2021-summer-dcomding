import heapq
import sys
input = sys.stdin.readline
def solve():
    N = int(input())
    values = [0] * N
    for i in range(N):
        values[i] = tuple(map(int,input().split()))
    values.sort()
    
    # heapq로 현재 사용 중인 자리의 끝나는 시간을 담고 있음.
    end_que = []
    # heapq로 현재 사용 가능한 자리의 idx를 담고 있음.
    idx_que = []
    # 각 자리별 사용 인원 수
    cache = [0] * N
    nxt_idx = 0
    
    for start,end in values:
        # 현재 사용 중인 인원이 있다면
        if len(end_que):
            # 그 중 가장 빨리 끝나는 사람을 찾는다.
            fastest_end, fastest_idx = end_que[0]
            # 만약 fastest_end가 start 보다 작다면 (즉 그 자리를 쓸 수 있다면)
            if fastest_end <= start:
                try:
                    # fastest_end가 start보다 커지거나 end_que가 빌때까지
                    # 계속 빼내서 idx_que에 넣음
                    while fastest_end <= start:
                        f_end, f_idx = heapq.heappop(end_que)
                        heapq.heappush(idx_que, f_idx)
                        fastest_end, fastest_idx = end_que[0]
                except:
                    pass  
            try:
                # idx_que에 value가 있다면 가장 빠른 자리를 찾는다.
                idx = heapq.heappop(idx_que)
                cache[idx] += 1
                heapq.heappush(end_que, (end, idx))
                continue
            except:
                pass
        # 사용중인 인원이 없거나, 빈자리가 없고 가장 빨리 끝나는 사람이 내 시작시간보다 느리면
        # 새로운 자리를 추가한다.
        cache[nxt_idx] += 1
        heapq.heappush(end_que, (end, nxt_idx))
        nxt_idx += 1
            
    print(nxt_idx)
    print(*cache[:nxt_idx])
solve()


