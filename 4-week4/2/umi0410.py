# 전형적인 그리디 문제. 매 학기 마다 푸는 것 같은데 매번 새로운 게 함정ㅋ
# 그리디는 max(이번 케이스를 포함안하고 이번 케이스를 추가했을 떄, 이번 케이스를 포함안했을 때)
# 약간 이런 느낌. 근데 쓰고 보니 이 문제는 그런 문젠 아니네.
# 가장 끝나는 시간이 빠른애가 제일 우선순위임. 그 다음은 가장 일찍 시작하는 애가 우선순위(이건 좀 이상하넴)
# 만약에 각 회의실 예약 케이스별로 가치가 달랐으면 어려웠곘지만 어차피 다 1팀으로 쳐서 가치가 낮았기 때문에 쉬움.
# N이 크니까 sys read line
import sys
input = sys.stdin.readline
N = int(input())
cases = [list(map(int, input().split())) for _ in range(N)]

cases.sort(key=lambda case: (case[1], case[0]))



last_end = 0
answer = 0
for start, end in cases:
    if last_end <= start:
        # print(start, end)
        last_end = end
        answer += 1

print (answer)
