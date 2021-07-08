import sys
from collections import deque
input = sys.stdin.readline
def solution():
    n = int(input())
    can_go = {}
    check = {}
    for i in range(n):
        start, end = input().split()
        try:
            can_go[start].append(end)
        except:
            can_go[start] = [end]
            
        try:
            check[start][end] = 1
        except:
            check[start] = {end: 1}
            
    def custom_rank(key):
        '''길이와 사전순을 기준으로 정렬'''
        try:
            check[key][idx]
            return (0,len(key), key)
        except:
            return (1, len(key), key)
    for idx in can_go:
        # fix
        
        can_go[idx] = deque(sorted(can_go[idx],key = custom_rank))
        
    cur = 'DCOM'
    result = ""
    while True:
        result += cur +' '
        try:
            nxt = can_go[cur].popleft()
        except:
            break
        cur = nxt
    print(result)
solution()