def solve():
    N = int(input())
    # 상태를 3개로 나누자. 
    # now, sub, main / 시작점, 둘다 아닌 곳, 도착점 
    moves = [[0,0,0] for i in range(N+1)]
    moves[0][2] = 1#[0,0,1]

    for i in range(1,N):
        [bef_now, bef_sub, bef_main] = moves[i - 1]
        # 점화식 성립
        moves[i] = [bef_now + bef_sub, bef_main + bef_now, bef_sub + bef_main + 1]
    print(sum([(i+1) * moves[N-1][i] for i in range(3)]))
solve()