import sys
from collections import deque
input = sys.stdin.readline
def solution():
    n = int(input())
    can_go = {}
    check = {}
    kinds = set()
    
    for i in range(n):
        start, end = input().split()   
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

    cur = 'DCOM'
    while True:
        print(cur, end =' ')
        cur_tickets = can_go[cur]
        nxt = cur_tickets.popleft()
        try:
            if cur_tickets and not check[nxt][end]:
                pass
        except:
            cur_tickets.append(nxt)
            nxt = cur_tickets.popleft()
        cur = nxt
        
        try:
            if not can_go[cur]:
                raise()
        except:
            print(cur, end =' ')
            break
solution()

     