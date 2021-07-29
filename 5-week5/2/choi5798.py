#dp[i] : i번째 위치에서 넣을 수 있는 상자의 최대 갯수 
n = int(input())
boxes = list(map(int, input().split()))

dp = [1 for _ in range(n)]
for i in range(1, n):
    for j in range(i):
        if boxes[j] < boxes[i]:
            dp[i] = max(dp[i], dp[j]+1) # +1 : i번째 상자 포함

print(max(dp))
