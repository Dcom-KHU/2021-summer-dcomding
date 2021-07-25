import sys

def solve():
    N = int(input())
    values =list(map(int,input().split()))
    
    #N = 3
    #values = [3,1,2]

    result = ""
    num = 0
    lo_max = [0] * (N + 2)
    hi_min = [0]* (N + 2)
    depth = [-1] * (N+1)
    for i in range(1,N+1):
        lo_max[i] = i - 1
        hi_min[i] = i + 1
    hi_min[N+1] = N+1
    
    def find_lo_max(cur,cur_stk):
        while lo_max[cur] < cur:
            cur_stk.append(cur)
            cur = lo_max[cur]
            
        return lo_max[cur]
    
    def find_hi_min(cur,cur_stk):
        while hi_min[cur] > cur:
            cur_stk.append(cur)
            cur = hi_min[cur]
            
        return hi_min[cur]
    for value in values:
        lo_stk = []
        lo = find_lo_max(value, lo_stk)
        
        hi_stk = []
        hi = find_hi_min(value, hi_stk)
        #print(lo_max)
        #print(hi_min)
        
        for h in hi_stk:
            lo_max[h] = value
        for l in lo_stk:
            hi_min[l] = value
        if 0 < lo < value:
            cur = lo
            lo_max[cur] = N+2
        elif value < hi < N+1:
            cur = hi
            hi_min[cur] = -1
        else:
            cur = value
            
        
        #print(value, cur, lo, hi, lo_stk,hi_stk)
        
        depth[value] = depth[cur] + 1
        num += depth[value]
        result += str(num) + "\n"
    #print(lo_max)
    #print(hi_min)
    #print(depth)
    print(result)
solve()
# 3 5 1 6 8 7 2 4
        