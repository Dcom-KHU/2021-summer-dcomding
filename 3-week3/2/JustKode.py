n = int(input())
list_var = []
dp = [0] * (n + 1)

for _ in range(n):
    list_var.append(list(map(int, input().split())))

for i in range(n):
    t, p = list_var[i]

    for j in range(i + t, n + 1):
        dp[j] = max(dp[j], dp[i] + p)

print(max(dp))