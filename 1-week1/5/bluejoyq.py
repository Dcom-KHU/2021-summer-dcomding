def solve():
    N = int(input())
    values = list(map(int, input().split()))
    
    # 원형이기 때문에 처음을 선택하는 경우와 선택하지 않는 경우를 다르게 세야함.
    
    # 처음 것을 안 고르는 경우
    cache = [0] * (N + 1)
    for i in range(1, N):
        cache[i] = max(cache[i-2] + values[i], cache[i-1])
    a = cache[N - 1]
    
    # 처음 것을 고르는 경우
    cache = [0] * (N + 3)
    for i in range(N - 1):
        cache[i] = max(cache[i-2] + values[i], cache[i-1])
    b = cache[N - 2]
    
    print(max(a,b))

solve()