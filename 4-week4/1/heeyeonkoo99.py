n,k=map(int,input().split())

moves=list(map(int,input().split()))
# print(moves)-체크용
board=[0 for _ in range(n)]
for i in range(n):
    board[i]=list(map(int,input().split()))
# print(board)-체크용

def solve():
    stack=[]
    count=0
    for m in moves:
        for i in range(len(board)):
            if board[i][m-1]!=0:
                if stack and stack[-1]==board[i][m-1]:
                    stack.pop()
                    count+=2
                else:
                    stack.append(board[i][m-1])
                board[i][m-1]=0 # 제대로 없애주기!
                break
    return count

print(solve())