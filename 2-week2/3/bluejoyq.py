import sys
from collections import deque
input = sys.stdin.readline
def solution():
    n = int(input())
    can_go = {}
    for i in range(n):
        start, end = input().split()
        try:
            can_go[start].append(end)
        except:
            can_go[start] = [end]
            
    def custom_rank(key):
        '''길이와 사전순을 기준으로 정렬'''
        return (len(key), key)
    
    for idx in can_go:
        can_go[idx] = deque(sorted(can_go[idx],key = custom_rank))

    result = []
    
    # 손선생님의 손길이 탄 코드입니다.
    funcStack = deque(["DCOM"])
    while funcStack:
        
        cur = funcStack[-1]
        try:
            funcStack.append(can_go[cur].popleft())
            if not can_go[cur]:
                del can_go[cur]  
        except:
            result.append(funcStack.pop())
            continue
        
    print(*result[::-1])
solution()