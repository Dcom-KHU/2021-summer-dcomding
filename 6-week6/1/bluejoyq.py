def solve():
    n = int(input())
    max_idx = 32
    cur = 1 << 32
    for i in range(32):
        if n & cur:
            break
        cur = cur >> 1
    print(cur)
solve()