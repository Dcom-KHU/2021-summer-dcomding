import sys
input = sys.stdin.readline
def solution():
    n = int(input())
    can_go = {}
    kinds = set()
    
    for i in range(n):
        start, end = input().split()   
        try:
            can_go[start].append(end)
        except:
            can_go[start] = [end]
            
    def rank(tmp):
        '''길이와 사전순을 기준으로 정렬'''
        return (len(tmp), tmp)
    for k in can_go:
        can_go[k].sort(key = rank)

    cur = 'DCOM'
    real_nxt_rank = ranks[real_nxt]
    while True:
        print(cur, end =' ')
        cur_tickets = can_go[cur]

        for i in range(len(cur_tickets)):
            nxt = cur_tickets[i]
            if not nxt:
                continue
            cur_tickets[i] = 0
        
        if not nxt:
            break
        cur = nxt
    
solution()
        