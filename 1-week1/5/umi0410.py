# 배낭 문제와 유사하지 않을까 싶다.
# 근데 배낭도 맨날 헷갈려서 얘도 헷갈린다.
# 예를 들어 한 집을 털면 다음 집은 못턴다.

# money[n]은 n번집을 턴 경우의 최대 돈

def solution(money):
    answers = [0] * len(money)
    # money는 3개 이상이랬음.
    # 처음 꺼 포함, 끝 꺼 포함 x
    answers[0] = money[0]
    answers[1] = money[0]
    for i in range(2, len(money)-1):
        answers[i] = max(answers[i-1], answers[i-2] + money[i])

    # 처음 꺼 포함 x, 끝 꺼 포함
    answers2 = [0] * len(money)
    # money는 3개 이상이랬음.
    answers2[0] = 0
    answers2[1] = money[1]
    for i in range(2, len(money)):
        answers2[i] = max(answers2[i - 1], answers2[i - 2] + money[i])
    return max(answers[-2], answers2[-1])


print(solution([1, 2, 3, 1,5,7,8,3,4]))