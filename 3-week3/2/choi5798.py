#dp(n) = max(dp(n), dp(i)+p(i))
#dp(n) : n일까지의 수익
#n일 이전에 받을 수 있는 모든 경우중 가장 큰값으로 갱신

n = int(input())
table = []
dp = []
answer = 0
for i in range(n):
    t, p = map(int, input().split())
    table.append((t, p))
    dp.append(p)

#날짜를 초과하지 않는 선에서 단순히 수익만 계산
for i in range(1, n):
    for j in range(i):
        if j + table[j][0] <= i:
            dp[i] = max(dp[i], dp[j]+table[i][1])
            #dp(i) = max(i일까지의 수익, j일까지의 수익 + i일의 수익)

#여기서 실제 그 외주를 맡았을 때 할 수 있는지 검사
for i in range(n):
    if i+table[i][0] <= n:
        if answer < dp[i]:
            answer = dp[i]
print(answer)

