import sys
from collections import deque
input = sys.stdin.readline
def solution():
    n = int(input())
    values = [0] * n
    kinds = set()
    for i in range(n):
        data = input().rstrip()
        values[i] = data
        kinds.add(data)
    goal = len(kinds)
    count_dict = {kind:0 for kind in kinds}
    
    cur = deque([])
    result = 123124121
    real_result = (0,0)
    for i in range(n):
        cur.append(values[i])
        count_dict[values[i]] += 1
        
        cur_goal = sum(map(bool,count_dict.values()))
        while goal == cur_goal:
            len_cur = len(cur)
            if result >len_cur :
                result = len_cur
                real_result = (i - len_cur + 1, i)
            last= cur.popleft()
            count_dict[last] -= 1
            cur_goal = sum(map(bool,count_dict.values()))          
    a,b = real_result
    print(a+ 1)
    print(b+1)
solution()