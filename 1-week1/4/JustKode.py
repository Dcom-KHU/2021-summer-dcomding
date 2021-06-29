n = int(input())
money = list(map(int, input().split()))

dp = [0 for i in range(n)]
dp[0], dp[1] = money[0], money[0]

for i in range(2, n - 1):
    dp[i] = max(dp[i - 1], dp[i - 2] + money[i])

dp2 = [0 for i in range(n)]
dp2[0], dp2[1] = 0, money[1]

for i in range(2, n):
    dp2[i] = max(dp2[i - 1], dp2[i - 2] + money[i])

print(max(dp[n - 2], dp2[n - 1]))