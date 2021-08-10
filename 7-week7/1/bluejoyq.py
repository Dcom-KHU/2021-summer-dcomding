def solve():
    # n개 2*2m
    N, M = map(int, input().split())
    blocks = list(map(int, input().split()))
    
    cur_balance_sum = blocks[N-1]
    for i in range(1, N):
        cur = N - 1 - i
        if blocks[cur] + M >cur_balance_sum / (i) > blocks[cur] - M:
            cur_balance_sum += blocks[cur]
        else:
            return 0
    
    return 1
print(solve())
            