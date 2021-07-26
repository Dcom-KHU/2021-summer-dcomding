import bisect
def solve():
    N = int(input())
    stk = [-1]
    # stack을 이용한 lis 찾기
    for value in map(int,input().split()):
        if value > stk[-1]:
            stk.append(value)
        else:
            stk[bisect.bisect_left(stk,value)] = value
    print(len(stk) - 1)
solve()