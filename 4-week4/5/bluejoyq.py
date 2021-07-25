import sys

def solve():
    N = 10000
    values = [i + 1 for  i in range(N)]
    
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
        while lo_max[cur] != cur:
            cur_stk.append(cur)
            cur = lo_max[cur]
            
        return cur
    
    def find_hi_min(cur,cur_stk):
        while hi_min[cur] != cur:
            cur_stk.append(cur)
            cur = hi_min[cur]
            
        return cur
    for value in values:
        #print(lo_max)
        #print(hi_min)
        #print(value)
        lo_stk = []
        lo = find_lo_max(value, lo_stk)
        
        hi_stk = []
        hi = find_hi_min(value, hi_stk)
            
        if 0 < lo < value:
            cur = lo
        elif value < hi < N+1:
            cur = hi
        else:
            cur = value
        #print(value, cur, lo, hi, lo_stk,hi_stk)
        depth[value] = depth[cur] + 1
        for l in lo_stk:
            lo_max[l] = lo
        for h in hi_stk:
            hi_min[h] = hi
        num += depth[value]
        result += str(num) + "\n"
    #print(lo_max)
    #print(hi_min)
    #print(depth)
    print(result)
solve()
# 3 5 1 6 8 7 2 4
        