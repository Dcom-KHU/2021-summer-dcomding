def solution(board, moves):
    result = [-1] # 2개가 팡 터지는 것을 위한 dummy
    pang_count = 0 # 2개가 만나 팡 하고 터진 카운트
    for move in moves:
        doll_code = 0
        for height in board:
            if height[move-1] != 0:
                doll_code = height[move-1]
                height[move-1] = 0
                break
        if doll_code != 0:
            if result[-1] == doll_code:
                result.pop()
                pang_count += 2
            else: result.append(doll_code)

    return pang_count

N, K = map(int, input().split())
moves = list(map(int, input().split()))
boards = [[n for n in map(int, input().split())] for _ in range(N)]

# print(moves)
# print(boards)
print(solution(boards, moves))