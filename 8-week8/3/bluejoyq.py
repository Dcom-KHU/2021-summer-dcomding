import heapq
import sys
input = sys.stdin.readline

def solution():
    n,m,k,start,end = map(int,input().split())
    edge = [[] for _ in range(n + 1)]
    mask_idx = {t : n for n, t in enumerate(traps)}
    traps = tuple(map(int,input().split()))

    for i in range(m):
        a, b, d = map(int,input().split())
        edge[a].append((b, d))
        edge[b].append((a, -d))

    # bfs
    heap = [(0, start, 0)]
    dist = {}
    answer = -1
    while heap:
        d, idx, mask = heapq.heappop(heap)
        if dist.get((idx, mask), None):
            continue

        dist[(idx, mask)] = d
        if idx == end:
            answer = d
            break;

        direction = 1
        if idx in traps and (mask & (1 << mask_idx[idx])):
            direction *= -1

        for near_idx, near_d in edge[idx]:
            if near_idx in traps and (mask & (1 << mask_idx[near_idx])):
                near_d *= -1

            if near_d * direction > 0:
                new_mask = mask
                if near_idx in traps:
                    if mask & (1 << mask_idx[near_idx]):
                        new_mask = mask & ~(1 << mask_idx[near_idx])
                    else:
                        new_mask = mask | (1 << mask_idx[near_idx]) 

                heapq.heappush(heap, (d + near_d * direction, near_idx, new_mask))


    return answer
print(solution())