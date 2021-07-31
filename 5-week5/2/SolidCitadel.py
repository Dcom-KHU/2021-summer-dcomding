n = int(input())
boxes = list(map(int, input().split()))

dp = list()
for i in range(n):
    dp.append(max([dp[j] for j in range(i) if boxes[j] < boxes[i]], default=0) + 1)

print(max(dp))
