a,b=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))

answer=list((set(A)-set(B)))+list((set(B)-set(A)))
print(len(answer))


