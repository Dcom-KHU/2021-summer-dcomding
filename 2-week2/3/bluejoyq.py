import sys
from collections import deque
sys.setrecursionlimit(1000000)
input = sys.stdin.readline
def solution(tickets):
    n = len(tickets)
    can_go = {}
    for i in range(n):
        start, end = tickets[i]
        try:
            can_go[start].append(end)
        except:
            can_go[start] = [end]
            
    def custom_rank(key):
        '''길이와 사전순을 기준으로 정렬'''
        return (len(key), key)

    for idx in can_go:
        can_go[idx] = deque(sorted(can_go[idx],key = custom_rank))
        
    
    
    def get_euler_circuit(cur, circuit):
        try:
            while can_go[cur]:
                nxt = can_go[cur].popleft()
                get_euler_circuit(nxt, circuit)
            del can_go[cur]
        except:
            circuit.appendleft(cur)
            return 0
        circuit.appendleft(cur)
        return 1
    start = 'ICN'
    result = []
    circuit = deque([])
    last = []
    if get_euler_circuit(start, circuit):
        result += circuit
    else:
        last = circuit
    for key in can_go:
        new_circuit = deque([])
        if get_euler_circuit(key, new_circuit):
            result += new_circuit
        else:
            last = new_circuit
    result += last
    return(result)