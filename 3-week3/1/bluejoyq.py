def solve():
    n, k = map(int, input().split())
    blocks = set(map(int, input().split()))
    print(min(k, len(blocks)))
solve()