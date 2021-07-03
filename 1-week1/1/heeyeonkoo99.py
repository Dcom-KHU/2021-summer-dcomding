#1주차 수업-1

n,k=map(int,input().split())
temp=list(map(int,input().split()))

for idx in range(1,k+1):
    if idx%2==1:
        temp.remove(min(temp))
    else:
        temp.remove(max(temp))

print(sum(temp))