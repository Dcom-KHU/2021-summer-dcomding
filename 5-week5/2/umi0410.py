N = int(input())
# 포함하지 않은 경우와 포함한 경우
# 개수와 마지막 사이즈
dp = [0 for _ in range(N)]

sizes = list(map(int, input().split())) # 맨 앞칸은 dummy

for i in range(N):
    # 나보다 작은 박스를 포함하며 끝난 경우 중 가장 많은 개수의 박스를 포함한 경우의 박수 개수
    before_max = 0
    for j in range(i):
        # 나보다 작은 박스였다면
        if sizes[j] < sizes[i]:
            before_max = max(dp[j], before_max)
    dp[i] = before_max + 1

print(max(dp))