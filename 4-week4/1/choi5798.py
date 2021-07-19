from collections import deque
def solution(board, moves):
    answer = 0
    ROW = len(board)
    queue = deque()
    for move in moves:
        for i in range(ROW):
            if board[i][move-1] != 0:
                queue.append(board[i][move-1])
                board[i][move-1] = 0
                break
        if len(queue) >=2 and queue[-1] == queue[-2]:
            queue.pop()
            queue.pop()
            answer += 2
            
    return answer
n, k = map(int, input().split())
moves = list(map(int, input().split()))
board = []
for _ in range(n):
    temp = list(map(int, input().split()))
    board.append(temp)
print(solution(board, moves))