# 끝까지 가는 경우 하나를 구하는 거면 DFS가 좋고
# 최단거리를 구해야하는 경우는 BFS가 좋다
# 이동할 때마다의 어떠한 aging 조건이 있으면 DFS가 그 이동의 상태를 관리하기 편하다.
# 근데 이번 꺼는 끝까지 가는 모든 경우긴 해서 별 상관없을 것 같은데 DFS로 해봄.
import copy

def solution(tickets):
    answers = []
    conns = {}
    length = 0
    for depart, dest in tickets:
        length += 1
        if conns.get(depart, None) == None:
            conns[depart] = [dest]
        else:
            conns[depart].append(dest)
    dfs(answers, length, 'DCOM', conns, ['DCOM'])

    return sorted(answers, key=lambda t: (len(t), t))[0]

def dfs(answers, length, depart, _conns, _visits):
    # print(_visits)
    if len(_visits) == length + 1:
        answers.append(_visits)
        return
    # get을 쓰지 않고 []로 접근하면 runtime error.
    # 해당 key가 출발지인 경우가 없을 수도 있기 때문
    for dest in _conns.get(depart, []):
        conns = copy.deepcopy(_conns)
        visits = copy.deepcopy(_visits)
        visits.append(dest)
        conns[depart].remove(dest)
        dfs(answers, length, dest, conns, visits)

# print(verify("()"))
# print(verify("() (())()()[({[]})]"))
tickets = []
for _ in range(int(input())):
    tickets.append(input().split())
print(' '.join(solution(tickets)))
# print(solution("]][["))
