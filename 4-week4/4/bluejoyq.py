import sys
input = sys.stdin.readline
def solve():
    N, L = map(int, input().split())
    board = [0] * N
    for i in range(N):
        board[i] = list(map(int, input().split()))
    result = 0
    for y in range(N):
        can_use = 1
        check = 1
        for x in range(N-1):
            # 경사로를 세울 수 있을 때
            #print(y,x, can_use, board[y][x],board[y][x  + 1] )
            if board[y][x] == board[y][x + 1] - 1 and can_use >= L:
                can_use = 1
            elif board[y][x] == board[y][x + 1] + 1:
                try:
                    for i in range(2,L + 1):
                        if board[y][x + 1] != board[y][x+i]:
                            raise()
                    can_use = - L + 1
                except:
                    check = 0
                    break
            elif board[y][x] == board[y][x + 1]:
                can_use += 1
            else:
                check = 0
                break
        if check:
            result += 1
            
    for x in range(N):
        can_use = 1
        check = 1
        for y in range(N-1):
            # 경사로를 세울 수 있을 때
            
            if board[y][x] == board[y + 1][x] - 1 and can_use >= L:
                can_use = 1
            elif board[y][x] == board[y + 1][x] + 1:
                try:
                    for i in range(2,L + 1):
                        if board[y + 1][x] != board[y + i][x]:
                            raise()
                        
                    can_use = - L + 1
                except:
                    check = 0
                    break
            elif board[y][x] == board[y + 1][x]:
                can_use += 1
            else:
                check = 0
                break
        if check:
            result += 1
    
    print(result)
solve()