import sys
import heapq
input = sys.stdin.readline
def solution():
    n = int(input())
    can_go = {}
    kinds = set()
    
    for i in range(n):
        a, b = input().split()
        
        try:
            can_go[a].append(b)
        except:
            can_go[a] = [b]
        kinds.add(a)
        kinds.add(b)
    
    def rank(tmp):
        return (len(tmp), tmp)
    kinds = list(kinds)
    ranks = {}
    num_of_kinds = len(kinds)
    visited = [[0] * num_of_kinds for i in range(num_of_kinds)]
    kinds.sort(key= rank)
    for i in range(num_of_kinds):
        ranks[kinds[i]] = i

    findings = []
    cur = 'DCOM'
    real_nxt ='DCOM'
    real_nxt_rank = ranks[real_nxt]
    while True:
        bef_rank = ranks[cur]
        cur_rank, cur = real_nxt_rank,real_nxt
        visited[bef_rank][cur_rank] = 1
        print(cur, end=' ')
        real_nxt = -1
        real_nxt_rank = 5001
        try:
            for nxt in can_go[cur]:
                nxt_rank= ranks[nxt]
                if visited[cur_rank][nxt_rank]:
                    continue
                if nxt_rank < real_nxt_rank:
                    real_nxt = nxt
                    real_nxt_rank = nxt_rank
            if real_nxt == -1:
                break
        except:
            break
    
solution()
        