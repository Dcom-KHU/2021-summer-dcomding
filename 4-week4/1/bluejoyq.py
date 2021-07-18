# cook your dish here
from collections import deque
def solution():
    n, k = map(int, input().split())
    moves = list(map(int,input().split()))
    
    values = [deque([]) for i in range(n)]
    for i in range(n):
        vals = list(map(int,input().split()))
        for j in range(n):
            if vals[j] == 0:
                continue
            values[j].appendleft(vals[j])
    
    goal = []
    result = 0
    for move in moves:
        move -= 1
        try:
            nxt = values[move].pop()
            goal.append(nxt)
            if goal[-1] == goal[-2]:
                goal.pop()
                goal.pop()
                result += 2
        except:
            continue
    print(result)
solution()