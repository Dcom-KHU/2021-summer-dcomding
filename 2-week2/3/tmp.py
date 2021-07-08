import sys
from collections import deque
input = sys.stdin.readline
def solution(tickets):
    n = int(len(tickets))
    can_go = {}
    check = {}
    kinds = set()
    for i in range(n):
        start, end = tickets[i]
        try:
            can_go[start].append(end)
            check[start][end] = 1
        except:
            can_go[start] = [end]
            check[start] = {end: 1}
            
    def rank(tmp):
        '''길이와 사전순을 기준으로 정렬'''
        return (len(tmp), tmp)
    
    
    for k in can_go:
        # fix
        can_go[k] = deque(sorted(can_go[k],key = rank))

    cur = 'ICN'
    result = []
    while True:
        result.append(cur)
        cur_tickets = can_go[cur]

        nxt = cur_tickets.popleft()
        try:
            if len(cur_tickets):
                check[nxt][cur]
        except:
            cur_tickets.append(nxt)
            nxt = cur_tickets.popleft()
        cur = nxt
        try:
            if not can_go[cur]:
                raise()
        except:
            result.append(cur)
            break
            
    return result

                          
#solution()