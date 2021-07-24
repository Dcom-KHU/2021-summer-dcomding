import sys

input = sys.stdin.readline


def solve():
    n = int(input())
    values = [0] * n
    for i in range(n):
        # end, start
        s, e = map(int, input().split())
        values[i] = [e, s]
    values.sort()  # end를 기준으로 정렬
    # print(values)

    cur = 0
    result = 0
    for end, start in values:
        if start < cur:
            continue
        result += 1
        cur = end

    print(result)


solve()