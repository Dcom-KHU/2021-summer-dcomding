#1주차 수업-1
import sys
n,k=map(int,sys.stdin.readline().split())
temp=list(map(int,sys.stdin.readline().split()))

for idx in range(1,k+1):
    if idx%2==1:
        temp.remove(min(temp))
    else:
        temp.remove(max(temp))

print(sum(temp))