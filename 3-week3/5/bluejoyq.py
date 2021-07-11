def solve():
    N = int(input()) +1 
    values = list(map(int, input().split()))
    values.insert(0,-1)
    # -1 기록
    stk = [0]
    result = -1
    for i in range(1,N):
        cur = values[i]
        while values[stk[-1]] >= cur:
            lst = stk.pop()
            result = max(result, (i - stk[-1] - 1) * values[lst] )
        stk.append(i)
    
    while len(stk) > 1:
        lst = stk.pop()
        result = max(result, (N - stk[-1] -1) * values[lst])
        
    print(result)
solve()