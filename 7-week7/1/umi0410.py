N, L = map(int, input().split())
dp = [0] * (N + 1)
coords = list(map(int, input().split()))
for i in range(N-2, -1, -1):
    dp[i+1] = dp[i+2] + coords[i+1]
    avg = dp[i+1] / (N - i - 1)
    if avg <= coords[i] - L or coords[i] + L <= avg:
        print(0)
        quit()
print(1)

