def solve():
    N = int(input())
    values = list(map(int, input().split()))
    
    # 원형이기 때문에 처음을 선택하는 경우와 선택하지 않는 경우를 다르게 세야함.
    
    cache = [0] * (N + 3)
    
    for i in range(1, N):
        cache[i+2] = max(cache[i+2], cache[i] + values[i])
        cache[i+3] = cache[i+3], cache[i] + values[i]
    
    a = max(cache[N-1:])
    cache = [0] * (N + 3)
    for i in range(N - 1):
        cache[i+2] = max(cache[i+2], cache[i] + values[i])
        cache[i+3] = cache[i] + values[i]
    b = max(cache[N-1:])
    print(max(a,b))

solve()