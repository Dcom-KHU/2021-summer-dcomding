# 전형적인 그리디 문제다 ㅎㅎ
N = int(input())
data = []
# 7일이라면 8칸, 인덱스는 [0,7]
greedy = [0] * (N + 1) # 한 칸은 dummy. max 값 연산을 위해
for _ in range(N):
    # (t, p)
    data.append(tuple(map(int, input().split())))

MAX = -1

for i, (tp) in enumerate(data):
    t, p = tp
    # 7일이라면 인덱스는 0(더미라 제외), 1,2,3,4,5,6,7
    # i는 7
    if i + t <= N:
        # 그리디는 항상 이번 거를 포함하지 않고 이전 거를 유지하는 것, 이번거를 포함하는 것 중의 더 이득인 것을 취함.
        greedy[i + t] = max(greedy[i + t], max(greedy[:i+1]) + p)
    # print(greedy[5])
# print(greedy)
print(max(greedy))
