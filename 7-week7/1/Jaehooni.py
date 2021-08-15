n, m = map(int, input().split())
blocks = list(map(int, input().split()))

def solve():
    compare = blocks[-1]
    center = 0
    for i, c in enumerate(reversed(blocks[:-1]), start=1):
        center = compare / i
        if (center <= c - m or center >= c + m):
            return 0

        compare += c

    return 1

print(solve())