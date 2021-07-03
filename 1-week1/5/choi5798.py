#점화식 dp[n] = max(dp[n-1], money[n]+dp[n-2])
#가운데집을 터는것과 양쪽을 털어서 합친것중 더 큰것 선택
n = int(input())
money = list(map(int, input().split()))
length = len(money)

dp1 = [0 for _ in range(length)] #0번째부터 터는 놈->마지막 포함x
dp2 = [0 for _ in range(length)] #1번째부터 터는 놈->마지막 포함o

dp1[0] = money[0]
dp1[1] = max(money[0], money[1])
for i in range(2, length-1):#마지막 포함x
    dp1[i] = max(dp1[i-1], dp1[i-2]+money[i])

dp2[0] = 0
dp2[1] = money[1]
for i in range(2, length):#마지막 포함o
    dp2[i] = max(dp2[i-1], dp2[i-2]+money[i])
print(max(max(dp1), max(dp2)))