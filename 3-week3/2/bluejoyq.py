def solve():
    n = int(input())
    cache = [0] * (30)
    for i in range(n):
        # t, p
        t,p = map(int,input().split())
        cache[i] = max(cache[i-1], cache[i])
        cache[i + t] = max(cache[i+t], cache[i] + p)

    print(max(cache[:n+1]))
    
solve()