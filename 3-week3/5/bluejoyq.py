def solve():
    N = int(input())
    values = list(map(int, input().split()))
    values.insert(0,-1)
    
    # -1 기록
    stk = [0]
    result = -1
    for i in range(1,N + 1):
        cur = values[i]
        while values[stk[-1]] > cur:
            lst = stk.pop()
            result = max(result, (i - lst ) * values[lst], (lst - stk[-1] ) * values[lst] )
        stk.append(i)
    
    while len(stk) > 1:
        lst = stk.pop()
        result = max(result, (N +1 - lst) * values[lst], (lst - stk[-1] ) * values[lst])
    
    print(result)

solve()